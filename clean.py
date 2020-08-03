import os
import shutil
from pathlib import Path

directories = False
files = 0
DLS_DIR = '{}/Downloads'.format(Path.home()) 
EXT_AUDIO_AND_MEDIA = ['.wav', '.mp3', '.mp4', '.mov', '.avi', '.wpl', '.png', '.jpg', '.jpeg', '.svg', '.gif']
EXT_DOCUMENTS = ['.docx', '.doc', '.pptx', '.ppt', '.txt', '.pdf', '.xlsx']
EXT_PROGRAMS_AND_INSTALLERS = ['.exe', '.msi', '.iso']
EXT_ZIPS = ['.zip', '.rar', '.7z']
EXT_MATH_AND_DESIGN = ['.vsdx', '.mcdx', '.m', '.ms14', '.ms13', '.mctx']
EXT_APPLICATIONS = ['.cpp', '.c', '.js', '.css', '.jar', '.html', '.bat', '.sh']
EXT_GARBAGE = ['.crdownload', '.vsix', '.lbr', '.curaprofile']
FOLDERS = ['Audio_Media', 'Documents', 'Programs_Installers', 'Zips', 'Math_Design', 'Applications']

def createDirectorys():
	global directories
	print('\nMAKING DIRECTORYS...')
	for folder in FOLDERS:
		if not os.path.exists(folder):
			directories = True
			os.makedirs(folder)
			print('Created a directory named {}'.format(folder))
	if not directories:
		print('ALL DIRECTORIES CREATED ALREADY...')

print('FOLDER CLEANING SERVICE')
print('\nCHANGING TO DIRECTORY {}\n'.format(DLS_DIR))
os.chdir(DLS_DIR)
createDirectorys()
print('ClEANING UP THE DIRECTORY AND SPLITTING FILES INTO FOLDERS...\n')
for file in os.listdir():
	name, ext = os.path.splitext(file)
	if ext in EXT_AUDIO_AND_MEDIA:
		shutil.move('{}{}'.format(name, ext), '{}'.format(FOLDERS[0]))
		print('Moving {}{} to {}'.format(name, ext, FOLDERS[0]))
		files += 1
	elif ext in EXT_DOCUMENTS:
		shutil.move('{}{}'.format(name, ext), '{}'.format(FOLDERS[1]))
		print('Moving {}{} to {}'.format(name, ext, FOLDERS[1]))
		files += 1
	elif ext in EXT_PROGRAMS_AND_INSTALLERS:
		shutil.move('{}{}'.format(name, ext), '{}'.format(FOLDERS[2]))
		print('Moving {}{} to {}'.format(name, ext, FOLDERS[2]))
		files += 1
	elif ext in EXT_ZIPS:
		shutil.move('{}{}'.format(name, ext), '{}'.format(FOLDERS[3]))
		print('Moving {}{} to {}'.format(name, ext, FOLDERS[3]))
		files += 1
	elif ext in EXT_MATH_AND_DESIGN:
		shutil.move('{}{}'.format(name, ext), '{}'.format(FOLDERS[4]))
		print('Moving {}{} to {}'.format(name, ext, FOLDERS[4]))
		files += 1
	elif ext in EXT_APPLICATIONS:
		shutil.move('{}{}'.format(name, ext), '{}'.format(FOLDERS[5]))
		print('Moving {}{} to {}'.format(name, ext, FOLDERS[5]))
		files += 1
	elif ext in EXT_GARBAGE:
		os.remove('{}{}'.format(name, ext))
		print('Deleting {}{}'.format(name, ext))
		files += 1
if files <= 0:
	print('\nTHERE WERE NO FILES TO CLEAN...')
else:
	print('\nDONE CLEANING UP! {} FILES WERE TREATED'.format(files))
nothing = input('Press enter to end program')