import shutil
import os
copytree = shutil.copytree("C:\\Users\\Z003YN0Y\\Desktop\\Dhanya",\
    "C:\\Users\\Z003YN0Y\\Desktop\\Dhanya_BACKUP")
print (copytree)
copy_to_file = shutil.copy('C:\\Users\\Z003YN0Y\\Desktop\\eggs.txt', \
    'C:\\Users\\Z003YN0Y\\Desktop\\delicious\\eggs.txt')
print (copy_to_file)
copy_to_folder = shutil.copy("C:\\Users\\Z003YN0Y\\Desktop\\Captur_828D.PNG",\
    "C:\\Users\\Z003YN0Y\\Desktop\\Config_LogDrives")
print (copy_to_folder)
