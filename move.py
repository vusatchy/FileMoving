import os
import shutil

size = 0
rootdir = "test"
destination_folder = "dest"

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for root, subFolders, files in os.walk(rootdir):
    for file in files:
        path = os.path.join(root, file)
        size += os.path.getsize(path)
        print("Moving: ", path)
        shutil.move(path, destination_folder)
print("All files size: ", size)
