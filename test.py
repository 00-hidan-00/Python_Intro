# go_loop = True
#
# while go_loop:
#         input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n")
#
#         if input_case == '1':
#             value_1 = input("Введи первое число:\n")
#             value_2 = input("Введи второе число:\n")
#             try:
#                 float_value_1 = float(value_1)
#                 float_value_2 = float(value_2)
#                 result = float_value_1 + float_value_2
#                 print("Ответ: ", result)
#             except ValueError:
#                 print('Это не похоже на цирфы :(\nПридётся начать с начала...')
#
#         elif input_case == '2':
#             value_1 = input("Введи первое число:\n")
#             value_2 = input("Введи второе число:\n")
#             try:
#                 float_value_1 = float(value_1)
#                 float_value_2 = float(value_2)
#                 result = float_value_1 - float_value_2
#                 print("Ответ: ", result)
#             except ValueError:
#                 print('Это не похоже на цирфы :(\nПридётся начать с начала...')
#
#         elif input_case == '3':
#             value_1 = input("Введи первое число:\n")
#             value_2 = input("Введи второе число:\n")
#             try:
#                 float_value_1 = float(value_1)
#                 float_value_2 = float(value_2)
#                 result = float_value_1 * float_value_2
#                 print("Ответ: ", result)
#             except ValueError:
#                 print('Это не похоже на цирфы :(\nПридётся начать с начала...')
#
#         elif input_case == '4':
#             value_1 = input("Введи первое число:\n")
#             value_2 = input("Введи второе число (ТОЛЬКО НЕ НОЛЬ!)\n")
#             try:
#                 float_value_1 = float(value_1)
#                 float_value_2 = float(value_2)
#                 result = float_value_1 / float_value_2
#                 print("Ответ: ", result)
#             except ValueError:
#                 print('Это не похоже на цирфы :(\nПридётся начать с начала...')
#             except ZeroDivisionError:
#                 print('Ну я же просил...\nДелить на ноль нельзя!' )
#         elif input_case != ('1', '2', '3', '4'):
#             print("Пожалуйста, выберете ОДИН из четырех вариантов !\nПридётся начать с начала...")
#         else:
#             print("Как ты это сделал ???...")
#
#         continue_request = input('\nЧто бы продолжить введите "y"\nЧто бы прекратить введите "n"\n')
#         if continue_request in 'n':
#             go_loop = False
#         elif continue_request != ('n', 'y'):
#             print("Следуйте инструкции !")

# my_str = "My name is John i'm 40"
#
# # for symbol in my_str:
# #     if not symbol.isupper():
# #         print(symbol)
#
# # for symbol in my_str:
# #     if symbol.islower() and symbol.isalpha() and symbol not in "eyuioa":
# #         print(symbol)
#
# result = my_str.find("John")
# print(result)
# my_str = "qwerty123456"

# for symbol in my_str:
#     print(symbol)
#
# for symbol in my_str[:6]:
#     print(symbol)
# #
# for index in range(5):
#     print(index)
# my_str = "My name is John i'm 40"
# # for index in range(len(my_str)):
# #     print(index)
# #
# for index, symbol in enumerate(my_str):
#     print(index, symbol)
# my_str = "My name is Anna, i'm 40. It is dog"
#
# for symbol in my_str:
#     if symbol.lower() in 'eyuioa':
#         print(symbol)



# result = my_str.find("John")
# print(result)

# my_list = [1, 2, 3,]
# index_value = 2
# value = 100

# if len(my_list) > index_value:
#     value = my_list[index_value]
# print(value)


########### так не нужно делать (ниже)
# try:
#     value = my_list[index_value]
#     print(value)
# except IndexError:
#     pass
#     print(value)

# my_list = []
# my_str = 'qwerty'
#
# for simbol in my_str:
#     my_list.append(simbol)
# print(my_list)

# file_path = 'home/zva/Pycharm/PythonIntro_14_03_22/lesson_6.py'
# parts = file_path.rsplit('lesson_')
# print(parts)


# my_list_1 = [1, 2, 3]
# my_list_2 = [10, 20, 30]
# my_result = []
# list_len = len(my_list_1)
# for index in range(list_len):
#     value_1 = my_list_1[index]
#     value_2 = my_list_2[index]
#     # my_result.append(value_1)
#     # my_result.append(value_2)
#     my_result += [value_1, value_2]
# print(my_result)
# my_list_1 = [1, 2, 3, 4]
# my_list_2 = [10, 20, 30]
# my_result = []
#
# list_len = min(len(my_list_1), len(my_list_2))
# for index in range(list_len):
#     value_1 = my_list_1[index]
#     value_2 = my_list_2[index]
#     my_result += [value_1, value_2]
#
# my_result += my_list_1[list_len:]
# my_result += my_list_2[list_len:]
#
# print(my_result)
# # ['ab', 'cd']
#
# my_str = 'adcdad'
# my_result = []
# my_str_1 = []
# my_str_2 = []
# my_str_1 += my_str[:2]
# my_str_2 += my_str[1:3]
# print(my_str_1,my_str_2)

# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
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

new_dict = {}
for key, value in my_dict_1.items():
    if key not in my_dict_2:
        new_dict[key] = value

for key, value in my_dict_2.items():
    if key not in my_dict_1:
        new_dict[key] = value

for key, value in my_dict_1.items():
    if key in my_dict_2:
        new_dict[key] = [value, my_dict_2[key]]
print(new_dict)

