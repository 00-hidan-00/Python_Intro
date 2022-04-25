# параметры по умолчанию
# позиционные и именнованые оргументы
# типы переменных
# импорт функций

def read_txt_file(filename='test.txt'):
    with open(filename, 'r') as my_file:
        data = my_file.read()
    return data
data = read_txt_file()
print(data)

###############################################

DEBUG_MODE = True

import string, random
from random import randint, choice

surnames_date = ["Shevchenko", "Vasilenko", "Ovcharenko", "Borisenko"]
domains_date = ["eu", "org", "best", "beer"]


def generation_email(domains, surnames, debug_mode=DEBUG_MODE):
    name = choice(surnames)
    domain = choice(domains)
    random_number = randint(100, 999)
    rand_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(randint(5, 7)))
    e_mail = (f'{name}.{random_number}@{rand_string}.{domain}').lower()
    if debug_mode:
        print(e_mail)
    return e_mail

email = generation_email(surnames=surnames_date, domains=domains_date)    # именнованые оргументы

###############################################

def read_txt_file(filename='test.txt', debug_mode=DEBUG_MODE):
    with open(filename, 'r', encoding='utf-8') as my_file:
        data = my_file.read()
    if debug_mode:
        print(data)
    return data
data = read_txt_file()

###############################################

def get_args(*args, **kwargs):
    for arg_value in args:
        print(arg_value)
    for kwarg_value in kwargs:
        print(kwarg_value, kwargs[kwarg_value])

get_args(1, 2, 'qwe', name="John", age=12)

###############################################

def read_txt_file(filename: str = 'test.txt', debug_mode: bool = True) -> str:
    with open(filename, 'r', encoding='utf-8') as my_file:
        data = my_file.read()
    if debug_mode:
        print(data)
    return data
data = read_txt_file("test.txt", True)

###############################################
# импорт функций


from utils.functions import read_txt_file_as_str, DEBUG_MODE
data = read_txt_file_as_str("test.txt")
print(f"{__name__=}")
print(data)

###############################################

import os
from utils.functions import read_txt_file_as_str

path = 'HomeWork'
list_dir = os.listdir(path)
# print(list_dir)

filename = 'Lesson_test.txt'
base_dir = ''
# data = read_txt_file_as_str(f'{path}/{base_dir}/{filename}')
# data = read_txt_file_as_str(os.path.join(path, base_dir, filename))
print(data)

for filename in list_dir:
    filepath = os.path.join(path, filename)
    if os.path.isdir(filepath):
        print(filepath)



# в 11 уроке доп к домашке в 10