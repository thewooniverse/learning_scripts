import shutil
import os


print(os.getcwd())
source_path = os.getcwd() + "/" + 'original.py'
dest_path = os.getcwd() + "/" + 'copy.py'
shutil.copyfile(source_path, dest_path)


# # specify the original file and destination file path
# original = './original.py'
# target = '/copy.py'

# # copy the file
# shutil.copyfile(original, target)