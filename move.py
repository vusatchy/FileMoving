import os
import shutil
from functools import reduce

root_folder = "test"
destination_folder = "dest"
allowed_folders = ["test2", "test4"]
sep = "\\"


def move(root_folder, destination_folder, allowed_folders):
    size = 0
    moving_history = []
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for root, _, files in os.walk(root_folder):
        current_folders = root.split(sep)[-1]
        if current_folders in allowed_folders:
            for file in files:
                path = os.path.join(root, file)
                size += os.path.getsize(path)
                print("Moving: ", path)
                shutil.move(path, destination_folder)
                moving_history.append((path, destination_folder))
    print("All files size: ", size)
    return moving_history


def test(root_folder, destination_folder, allowed_folders):
    moving_history = move(root_folder, destination_folder, allowed_folders)
    for root, _, files in os.walk(root_folder):
        current_folders = root.split("\\")[-1]
        if current_folders in allowed_folders:
            if len(files) == 0:
                print(root, " : is empty")
            else:
                raise Exception(root + " : is not empty")
    print("Test passed")
    # move back
    for pair in moving_history:
        path = pair[0]
        destination = pair[1]
        file = path.split(sep)[-1]
        from_path = os.path.join(destination, file)
        to_path = reduce(os.path.join, path.split(sep)[:-1])
        shutil.move(from_path, to_path)


test("test", "dest", ["test2", "test4"])
