import os
from string import ascii_lowercase as alphabet
from random import shuffle


def create_dir(dirname):
    # os.mkdir(dirname)   # старье
    os.makedirs(dirname, exist_ok=True)

def create_files(dirname):
    for symbol in alphabet:
        create_file(dirname, symbol)

def create_file(dirname, symbol):
    file_path = os.path.join(dirname, f'{symbol}.txt')
    with open(file_path, 'w') as txt_file:
        txt_file.write(alphabet.replace(symbol, symbol.upper()))


def do_tanos_click(dirname):
    dir_list = os.listdir(dirname)
    shuffle(dir_list)
    for filename in dir_list[::2]:
        filepath = os.path.join(dirname, filename)
        os.remove(filepath)


dirname = 'alphabet'
create_dir(dirname)
create_files(dirname)
do_tanos_click(dirname)
