import os

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
        if os.path.isdir(filepath):
            dirs_list.append(filename)
    files_dirs_names = {'filenames': files_list,
                        'dirnames': dirs_list}
    return files_dirs_names


result_1 = return_files_dirs_names(path)

# 2

status = False


def return_files_dirs_names_sort(result_1, status) -> dict:
    for key, value in result_1.items():
        if key == 'filenames':
            files_list = value
        if key == 'dirnames':
            dirs_list = value
    if status == True:
        files_dirs_names_dict_sort = {'filenames': sorted(files_list),
                                      'dirnames': sorted(dirs_list)}
    else:
        files_dirs_names_dict_sort = {'filenames': sorted(files_list, reverse=True),
                                      'dirnames': sorted(dirs_list, reverse=True)}
    return files_dirs_names_dict_sort


result_2 = return_files_dirs_names_sort(result_1, status)

# 3

file_name = 'test.py'


def add_files_dirs_names(result_1, file_name) -> dict:
    for key, value in result_1.items():
        if key == 'filenames':
            files_list = value
        if key == 'dirnames':
            dirs_list = value
    if os.path.isfile(file_name):
        files_list.append(file_name)
    if os.path.isdir(file_name):
        dirs_list.append(file_name)
    add_files_dirs_names = {'filenames': files_list,
                            'dirnames': dirs_list}
    return add_files_dirs_names


result_3 = add_files_dirs_names(result_1, file_name)
