import os

def write_file(file_name, file_content):
    file_path = f"{file_name}.txt"
    dir_name = os.path.dirname(file_path)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name, exist_ok=True)
    with open(file_path, mode='w', encoding='utf-8') as fi:
        return fi.write(file_content)

def append_file(file_name, append_content):
    file_path = f"{file_name}.txt"
    dir_name = os.path.dirname(file_path)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name, exist_ok=True)
    with open(file_path, mode='a', encoding='utf-8') as fi:
        return fi.write(append_content)

def read_file(file_name):
    file_path = f"{file_name}.txt"
    with open(file_path, mode='r', encoding='utf-8') as fi:
        return fi.read()