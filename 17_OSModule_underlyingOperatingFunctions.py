import os
from datetime import datetime

#Shows attributes and methods
print(dir(os))

#Shows current working directory
print(os.getcwd())

#Shifts past working directory to new directory this does'nt means that 
#this python file moves to that location
os.chdir('C:/Users/user/Desktop/Programming/Python/Python Programming/')
print(os.getcwd())

#This shows files and directories in the current directory
print(os.listdir())

'''
#Mkdir creates the file but not the subfolders like makedirs you can execute only ones
os.mkdir('FileCreatedByOS')
print(os.listdir())
'''

'''
#Makedirs must include subfolders otherwise error occurs
os.makedirs('FileCreatedByOSByMakedirs/SubFolder')


print(os.listdir())

#Removes directories
os.rmdir('FileCreatedByOS')
os.removedirs('FileCreatedByOSByMakedirs/SubFolder')
'''

print(os.listdir())
'''
os.mkdir('FileCreatedByOS')
print(os.listdir())
'''
'''
#Renames the file from name called FileCreatedByOS to Renamed file
os.rename('FileCreatedByOS','Renamed file')
print(os.listdir())
'''

#To know more about the file or directory 
print(os.stat('AI'))

#To print secefic stat st_mtime is modification time
print(os.stat('AI').st_mtime)

#To print datetime of modification
mod_time=os.stat('AI').st_mtime
print(datetime.fromtimestamp(mod_time))

#To check all the directory path,dirnames,filenames within the walk directory
for dirpath,dirnames,filenames in os.walk('C:/Users/user/Desktop/Programming/Python/Python Programming/'):
	print('current path: ',dirpath)
	print('dirnames: ',dirnames)
	print('filenames: ',filenames)

#It prints the how directory location for not the result must come
#C:/Users/user/Desktop/Programming/Python/
print(os.environ.get('HOME'))

#Shows the base name or last subdirectory
print(os.path.basename('C:/Users/user/Desktop/Programming/Python/Python Programming/Programs/Episode9_Importing_modules_and_Exploring_Libuary/Mymodule.py'))

#Shows the directory path above the base name
print(os.path.dirname('C:/Users/user/Desktop/Programming/Python/Python Programming/Programs/Episode9_Importing_modules_and_Exploring_Libuary/Mymodule.py'))

#To show both the name and directory
print(os.path.split('C:/Users/user/Desktop/Programming/Python/Python Programming/Programs/Episode9_Importing_modules_and_Exploring_Libuary/Mymodule.py'))

#Check wether the path exist or not
print(os.path.exists('exist/myname'))

#check wether it is a file or not
print(os.path.isfile('C:/Users/user/Desktop/Programming/Python/Python Programming/Programs/Episode9_Importing_modules_and_Exploring_Libuary/Mymodule.py'))

#Check wether it is a director or not
print(os.path.isdir('C:/Users/user/Desktop/Programming/Python/Python Programming/Programs/Episode9_Importing_modules_and_Exploring_Libuary'))

#Splits the extension of the file
print(os.path.splitext('C:/Users/user/Desktop/Programming/Python/Python Programming/Programs/Episode9_Importing_modules_and_Exploring_Libuary/Mymodule.py'))

