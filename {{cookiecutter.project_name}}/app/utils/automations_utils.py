import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def remove_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)