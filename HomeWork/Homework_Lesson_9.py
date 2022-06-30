# 1
my_list = ['23', 'wqr', "214", '24', 'qw']

def create_new_list(initial_list):
    result = []
    for index, symbol in enumerate(initial_list):
        if index % 2 == 0:
            result.append(symbol[::-1])
        else:
            result.append(symbol)
    return result
# 2
my_list = ['aqfwqf', 'wqwq', 'a532', '1qwq', 'aaaaaa']

def create_list_with_first_a(initial_list):
    result = []
    for symbol in initial_list:
        if symbol[0] == "a":
            result.append(symbol)
    return result
# 3
my_list = ['qfwaqf', 'wqwq', '5a32', '1qwq', 'aaaaaa', 'fe1awqf', '21421']

def create_list_with_a(initial_list):
    result = []
    for symbol in initial_list:
        if "a" in symbol:
            result.append(symbol)
    return result
# 4
my_list = [1, 2, 3, "11", "ab", "22", 33]

def create_list_with_str(initial_list):
    result = [value for value in initial_list if type(value) == str]
    return result

# 5
my_str = '11sssssssss222E/./12D11'


def create_list_single_symbol(initial_str):
    result = []
    for symbol in set(initial_str):
        if initial_str.count(symbol) == 1:
            result.append(symbol)
    return result
# 6
my_str_1 = "a1234tt"
my_str_2 = "a1234rr"

def create_list_identical_symbols(initial_str_1, initial_str_2):
    result = list(set(initial_str_1).intersection(set(initial_str_2)))
    return result

# 7
my_str_1 = 'aaaaawwfaaaafdv'
my_str_2 = 'dasfff2v'

def create_list_individual_symbols(initial_str_1, initial_str_2):
    result = []
    for symbol in set(initial_str_1).intersection(set(initial_str_2)):
        if my_str_1.count(symbol) == 1 and initial_str_2.count(symbol) == 1:
            result.append(symbol)
    return result
# 8
import string, random
from random import randint, choice
surnames_date = ["Shevchenko", "Vasilenko", "Ovcharenko", "Borisenko"]
domains_date = ["eu", "org", "best", "beer"]

def generation_email(surnames, domains):
    name = choice(surnames)
    domain = choice(domains)
    random_number = randint(100, 999)
    rand_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(randint(5, 7)))
    e_mail = (f'{name}.{random_number}@{rand_string}.{domain}').lower()
    return e_mail
