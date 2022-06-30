import os


import shutil

# 1


def return_files_dirs_names(path: str) -> dict:
    list_dir = os.listdir(path)
    files_list = []
    dirs_list = []
    for filename in list_dir:
        filepath = os.path.join(path, filename)
        if os.path.isfile(filepath):
            files_list.append(filename)
        elif os.path.isdir(filepath):
            dirs_list.append(filename)
    files_dirs_names = {'filenames': files_list,
                        'dirnames': dirs_list}
    return files_dirs_names


result_1 = return_files_dirs_names('from_test_dir')
print(result_1)
# 2

status = False


def return_files_dirs_names_sort(result_1: dict, status=True) -> dict:
    if status:
        result_1["filenames"].sort()
        result_1["dirnames"].sort()
    else:
        result_1["filenames"].sort(reverse=not status)
        result_1["dirnames"].sort(reverse=not status)
    return result_1


result_2 = return_files_dirs_names_sort(result_1, status)
print(result_2)


# 3


def add_files_dirs_names(result_1: dict, file_name: str) -> dict:
    key = "filenames" if '.' in file_name else "dirnames"

    result_1[key].append(file_name)
    return result_1


result_3 = add_files_dirs_names(result_1, 'testtw.qfw')
print(result_3)


# 4


def create_dir(result_1: dict, dir_name: str):
    for value in result_1["filenames"]:
        dir_list = os.listdir(dir_name)
        if not value in dir_list:
            with open(os.path.join(dir_name, value), 'w') as file:
                file.close()
    for value in result_1["dirnames"]:
        os.makedirs(os.path.join(dir_name, value), exist_ok=True)


create_dir(result_1, 'to_test_dir')
