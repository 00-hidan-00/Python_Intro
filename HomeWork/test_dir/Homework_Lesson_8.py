# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate или range.

my_list = ['23', 'wqr', "214", '24', 'qw']
box = []

for index in range(len(my_list)):
    symbol = my_list[index]
    if index % 2 == 0:
        box.append(symbol[::-1])
    else:
        box.append(symbol)
print(box)

# box = my_list.copy()
# for index, str_ in enumerate(my_list):
#     if index % 2:
#         box[index] = str_[::-1]

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".

my_list = ['aqfwqf', 'wqwq', 'a532', '1qwq', 'aaaaaa']
box = []
for symbol  in my_list:
    if symbol[0] == "a":
        box.append(symbol)
print(box)

# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ['qfwaqf', 'wqwq', '5a32', '1qwq', 'aaaaaa', 'fe1awqf', '21421']
box = []
for symbol in my_list:
    if "a" in symbol:
        box.append(symbol)
print(box)

# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Создать список и поместить туда имя самого молодого человека.
# Если возраст совпадает - поместить все имена самых молодых.
# б) Создать список и поместить туда самое длинное имя. Если длина имени совпадает - поместить все такие имена.
# в) Посчитать среднее количество лет всех людей из начального списка.
################################################
# а)
persons = [{"name": "Charlotte", "age": 15},
           {"name": "Emma", "age": 7},
           {"name": "Olivia", "age": 45},
           {"name": "Charlotte", "age": 15},
           {"name": "Charlotte", "age": 15},
           ]
min_age_list = []
min_age_name = []
for person in persons:
    min_age_list.append(person['age'])
min_age = min(min_age_list)
for person in persons:
    if min_age == person["age"]:
        min_age_name.append(person['name'])
print(min_age_name)
# ################################################
# б)
names = []
max_name = []
for person in persons:
    names.append(len((person['name'])))
max_len_name = max(names)
for person in persons:
    if max_len_name == len(person['name']):
        max_name.append(person['name'])
print(max_name)
################################################
# в)
ages = []
for person in persons:
    ages.append(person['age'])
average_age = sum(ages) / len(ages)
print(average_age)

################################################
# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
my_dict_1 = {'city': "Dnipro",
             'street': 'Polya',
             'zip': 49000,
             '1': 2,
             "few": 124,
             }
my_dict_2 = {'name': 'John',
             "age": 24,
             'Job': 'president',
             'street': 'Polya',
             'zip': 49000,
             '1': 2,
             '2': 22,
             "few": 124,
             }
# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.

box = []
for key in my_dict_1:
    if key in my_dict_2:
        box += [key]
print(box)


# result_1 = list(set(my_dict_1.keys()).intersection(set(my_dict_2.keys())))

# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.

box = []
for key in my_dict_1:
    if key not in my_dict_2:
        box += [key]
print(box)

#V2
# result_2 = list(set(my_dict_1.keys()).difference(set(my_dict_2.keys())))

# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.

new_dict = {}
for key, value in my_dict_1.items():
    if key not in my_dict_2:
        new_dict[key] = value
print(new_dict)

#V2
# result_3 = {key: my_dict_1[key] for key in result_2}

# result_3 = {}
# for key in result_2:
#     result_3[key] = my_dict_1[key]

# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

new_dict = {}
for key in my_dict_1:
    if key in my_dict_2:
        new_dict[key] = [my_dict_1[key], my_dict_2[key]]
    else:
        new_dict[key] = my_dict_1[key]
for key in my_dict_2:
    if key not in my_dict_1:
        new_dict[key] = my_dict_2[key]
print(new_dict)

#V2
# result_4 = my_dict_1.copy()
# for key in my_dict_2:
#     if key in result_4:
#         result_4[key] = [result_4[key], my_dict_2[key]]
#     else:
#         result_4[key] = my_dict_2[key]
# print(result_4)