import os
from string import ascii_lowercase as alphabet
from random import shuffle


class PlayWithFolder:
    def __init__(self, dirname):
        self.dirname = dirname
        self.create_dir()

    def create_dir(self):
        os.makedirs(self.dirname, exist_ok=True)

    def create_files(self):
        for symbol in alphabet:
            self.create_file(symbol)

    def create_file(self, symbol):
        file_path = os.path.join(self.dirname, f'{symbol}.txt')
        with open(file_path, 'w') as txt_file:
            txt_file.write(alphabet.replace(symbol, symbol.upper()))

    def do_tanos_click(self):
        dir_list = os.listdir(self.dirname)
        shuffle(dir_list)
        for filename in dir_list[::2]:
            filepath = os.path.join(self.dirname, filename)
            os.remove(filepath)


worker = PlayWithFolder('alphabet_3')
