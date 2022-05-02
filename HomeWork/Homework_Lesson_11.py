import os
# import shutil

# 1

path = 'from_test_dir'


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
        result_1["filenames"].sort()
        result_1["dirnames"].sort()
    else:
        result_1["filenames"].sort(reverse=True)
        result_1["dirnames"].sort(reverse=True)
    return result_1


result_2 = return_files_dirs_names_sort(result_1, status)
print(result_2)
# 3

file_name = 'testtw.qfw'


def add_files_dirs_names(result_1, file_name) -> dict:
    if '.' in file_name:
        result_1["filenames"].append(file_name)
    else:
        result_1["dirnames"].append(file_name)
    return result_1


result_3 = add_files_dirs_names(result_1, file_name)

# 4

dir_name = 'to_test_dir'


def create_dir(result_1, dir_name):
    for value  in result_1["filenames"]:
        dir_list = os.listdir(dir_name)
        if not value in dir_list:
            with open(os.path.join(dir_name, value), 'w') as file:
                file.close()
    for value in result_1["dirnames"]:
        os.makedirs(os.path.join(dir_name, value), exist_ok=True)

create_dir(result_1, dir_name)


# функция сохдает файлы из заданой директории в изначальную
# dir_name = 'from_test_dir'
#
#
# def create_dir(result_1, dir_name):
#     for filename in os.listdir(dir_name):
#         for value in result_1.values():
#             if filename not in value:
#                 if os.path.isfile(os.path.join(dir_name, filename)):
#                     shutil.copy(os.path.join(dir_name, filename), os.path.join(path, filename))
#                 elif os.path.isdir(os.path.join(dir_name, filename)):
#                     shutil.copytree(os.path.join(dir_name, filename), os.path.join(path, filename), dirs_exist_ok=True)
#
#
# create_dir(result_1, dir_name)
