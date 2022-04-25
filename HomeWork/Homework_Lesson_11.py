import os
from pathlib import Path

# 1

path = 'test_dir'


def return_files_dirs_names(path) -> dict:
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


result_1 = return_files_dirs_names(path)

# 2

status = False


def return_files_dirs_names_sort(result_1, status) -> dict:
    if status:
        files_dirs_names_dict_sort = {'filenames': sorted(result_1["filenames"]),
                                      'dirnames': sorted(result_1["dirnames"])}
    else:
        files_dirs_names_dict_sort = {'filenames': sorted(result_1["filenames"], reverse=True),
                                      'dirnames': sorted(result_1["dirnames"], reverse=True)}
    return files_dirs_names_dict_sort


result_2 = return_files_dirs_names_sort(result_1, status)

# 3

file_name = 'tguuhnestpy'


def add_files_dirs_names(result_1, file_name) -> dict:
    add_files_dirs_names = {'filenames': result_1["filenames"],
                            'dirnames': result_1["dirnames"]}
    if '.' in file_name:
        result_1["filenames"].append(file_name)
    else:
        result_1["dirnames"].append(file_name)
    return add_files_dirs_names


result_3 = add_files_dirs_names(result_1, file_name)

# 4

new_file_name = 'testt'


def create_dir(result_1, new_file_name):
    for value in result_1.values():
        if new_file_name not in value:
            os.makedirs(Path(path, new_file_name), exist_ok=True)


create_dir(result_1, file_name)
