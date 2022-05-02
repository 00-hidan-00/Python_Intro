import os


class PlayWithFolder:
    def __init__(self, path: str):
        self.path = path
        self.status = False
        self.file_name = 'new_test_file.py'
        self.dir_name = 'to_test_dir'
        self.result_1 = self.return_files_dirs_names()
        self.result_2 = self.return_files_dirs_names_sort()
        self.result_3 = self.add_files_dirs_names()
        self.create_dir()

    # 1

    def return_files_dirs_names(self) -> dict:
        list_dir = os.listdir(self.path)
        files_list = []
        dirs_list = []
        for filename in list_dir:
            filepath = os.path.join(self.path, filename)
            if os.path.isfile(filepath):
                files_list.append(filename)
            elif os.path.isdir(filepath):
                dirs_list.append(filename)
        files_dirs_names = {'filenames': files_list,
                            'dirnames': dirs_list}
        return files_dirs_names

    # 2

    def return_files_dirs_names_sort(self) -> dict:
        if self.status:
            self.result_1["filenames"].sort()
            self.result_1["dirnames"].sort()
        else:
            self.result_1["filenames"].sort(reverse=True)
            self.result_1["dirnames"].sort(reverse=True)

        return self.result_1

    # 3

    def add_files_dirs_names(self) -> dict:
        if '.' in self.file_name:
            self.result_1["filenames"].append(self.file_name)
        else:
            self.result_1["dirnames"].append(self.file_name)

        return self.result_1

    # 4

    def create_dir(self):
        dir_list = os.listdir(self.dir_name)
        for value in self.result_1["filenames"]:
            file_path = os.path.join(self.dir_name, value)
            if not value in dir_list:
                with open(file_path, 'w') as file:
                    file.close()
        for value in self.result_1["dirnames"]:
            file_path = os.path.join(self.dir_name, value)
            os.makedirs(file_path, exist_ok=True)


worker = PlayWithFolder('from_test_dir')
