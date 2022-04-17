# 1
my_list = ['23', 'wqr', "214", '24', 'qw']


def crtNewList(initial_list):
    result = []
    for index, symbol in enumerate(initial_list):
        if index % 2 == 0:
            result.append(symbol[::-1])
        else:
            result.append(symbol)
    return result


# 2
my_list = ['aqfwqf', 'wqwq', 'a532', '1qwq', 'aaaaaa']


def crtList_withFist_a(initial_list):
    result = []
    for symbol in initial_list:
        if symbol[0] == "a":
            result.append(symbol)
    return result


# 3
my_list = ['qfwaqf', 'wqwq', '5a32', '1qwq', 'aaaaaa', 'fe1awqf', '21421']


def crtList_with_a(initial_list):
    result = []
    for symbol in initial_list:
        if "a" in symbol:
            result.append(symbol)
    return result


# 4
my_list = [1, 2, 3, "11", "ab", "22", 33]


def crtList_withStr(initial_list):
    result = [value for value in initial_list if type(value) == str]
    return result


# 5
my_str = '11sssssssss222E/./12D11'


def crtList_singleSymbol(initial_str):
    result = []
    for symbol in set(initial_str):
        if initial_str.count(symbol) == 1:
            result.append(symbol)
    return result


# 6
my_str_1 = "a1234tt"
my_str_2 = "a1234rr"


def crtList_identicalSymbols(initial_str_1, initial_str_2):
    result = list(set(initial_str_1).intersection(set(initial_str_2)))
    return result


# 7
my_str_1 = 'aaaaawwfaaaafdv'
my_str_2 = 'dasfff2v'


def crtList_individualSymbols(initial_str_1, initial_str_2):
    result = []
    for symbol in set(initial_str_1).intersection(set(initial_str_2)):
        if my_str_1.count(symbol) == 1 and initial_str_2.count(symbol) == 1:
            result.append(symbol)
    return result


# 8
surnames = ["Shevchenko", "Vasilenko", "Ovcharenko", "Borisenko"]
domains = ["eu", "org", "best", "beer"]


def generation_email():
    import string, random
    from random import randint, choice
    name = choice(surnames)
    domain = choice(domains)
    random_number = randint(100, 999)
    rand_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(randint(5, 7)))
    e_mail = (f'{name}.{random_number}@{rand_string}.{domain}').lower()
    return e_mail

