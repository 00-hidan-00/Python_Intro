# result = round(1.2 * 3, 2)
# print(result)
#
# result = 7 % 2 == 0  # узнать четное число или нет
# print(result)
#
# a = 10
# b = 5
# c = 7
# p = (a + b + c) / 2
#
# area = (p*(p-a)*(p-b)*(p-c))**0.5
# print(area)
#
#
# #### str
#
# # экранизация символов с помощью \ ("\'", "\\")
#
#
# str = "I'm Elias and I'm a \"strong\" programmer"
# print(str)
#
# str = "C:Users\\EngineerSpock\\file.py"
# print(str)
#
# ##########################################################
#
# str = r'C:Users\EngineerSpock\file.py'   # чош бы не экранировать каждый раз \
# print(str)
#
#
# ##########################################################
#
# ## Конкатенация строк
#
# hello = 'hello'
# world = 'world'
#
# print(hello + " " + world)
# print("%s %s" % (hello, world))
# print("{} {}".format(hello, world))
#
# ##########################################################
#
# ## Функции string
#
# x = "hello, my name is Elias, 123abc"
#
# result = len(x)
# print(result)
#
# result = x[len(x)-1]     # шаг
# print(result)
#
# result = x.count('l')      # посчет символов в строке
# print(result)
#
# result = x.capitalize()     # Делает первый символ в верхний регистр, а остальные в нижний
# print(result)
#
# result = x.upper()     # Делает все символы в верхнем регистре
# print(result)
#
# result = x.lower()     # Делает все символы в нижгем регистре
# print(result)
#
# result = x.isupper()     # справшивает, находятся ли все символы в веррхнем регистре
# print(result)
#
# result = x.islower()     # справшивает, находятся ли все символы в нижнем регистре
# print(result)
#
# result = x.find('l', 5, 10)     # ищет на каком метсе нужный нам символ, так же можно указать откудаго и до кудаго искать
# print(result)
#
# print(x.find('l'))
# print(x.find('l', 5))
# print(x.find('l', 5, 10))
# print(x.find('m', 7, 15))
# print(x.find('m', 8, 10))
#
# result = x.find('my')
# print(result)
#
# result = x.isalnum()         # гооворит, состоит ли строка из букв и чисел
# print(result)
#
# result = x.isalpha()           # гооворит, состоит ли строка из букв
# print(result)
#
# result = x.isspace()            # проверяет, пустая ли строка (состоит ли из одних проблелов)
# print(result)
#
# result = x.strip(' ')             # Удаление пробельных символов в начале и в конце строки
# print(result)
#
# x = ' a a '                    # проверить, пустая ли строка V1.0 (лучший способ)
# print(x.strip(' ') == '')
#
# emty_string = ''               # проверить, пустая ли строка V2.0
# if not emty_string:
#     print('not empty')
# else:
#     print('empty')
#
#
# h = "hello"
# result = h.startswith('he')       # проверяет, начинается ли строка с нужных нам сиволов
# result2 = h.endswith('lo')        # проверяет, заканчивается ли строка с нужных нам сивол
# print(result, result2)
#
# h = "hello hello hello"             # разбивает входящую строку на части используя раазделитель (сепаратор)
# result = h.split('l')               # превращает строку в слисок
# print(result)
#
# data = "12;10;9;10;321;215"
# separated_date = data.split(';')
# print(separated_date)
#
# python = 'Pyrhon is fun'            # Возвращает кортеж, содержащий часть перед первым шаблоном,
# print(python.partition('is '))      # сам шаблон, и часть после шаблона. Если шаблон не найден,
# print(python.partition('not '))     # возвращается кортеж, содержащий саму строку, а затем две пустых строки
# python = "Pyrhon is fun, isn't it"
# print(python.partition('is'))
#
#
# ## Форматирование строк
#
# print("My name is {}".format("Elias"))
#
# my_name = "Elias"
# result = "My name is {}".format(my_name)
# print(result)
#
# my_name = "Elias"
# result = "My name is "f'{my_name}'
# print(result)
#
# my_name = "Elias"
# result = "My name is {} and I'm {}".format(my_name, 30)
# print(result)
#
# my_name = "Elias "
# result = "My name is {1} and I'm {0}".format(my_name, 30)
# print(result)
#
# pi = 3.1415
# my_str = "Pi equals {pi:1.2f}".format(pi=pi)           # обрезать сотые
# print(my_str)
#
#
# pi = 3.1415
# my_str = "Pi equals " f'{pi:.2f}'         # обрезать сотые
# print(my_str)
#
# ## Операторы сравнения
#
# x = "String"
# y = "string"
#
# result = x.lower() == y.lower()
# print(result)
#
# result = 1 < 2 < 3
# print(result)
#
# result = 1 > 2 and 2 < 3
# print(result)
#
# result = 1 > 2 or 2 < 3
# print(result)
#
# ## !!!!
# is_admin = True # pretend asking for security  module
# file_exists = True # pretend asking OS about file existence
#
# should_open_file = is_admin and file_exists
# print(should_open_file)
#
# is_admin = False
# if not is_admin:
#     print("not an admin")
#
# if is_admin == False:
#     print("not an admin")
#
# ##  Операции над файлами
#
# import os
# dirpath = os.getcwd()
# print(dirpath)
#
#
# file = open("file_test.txt")
# data = file.read()
# print(data)
#
# file.seek(0)
#
# data = file.read()
# print(data)
#
#
# lines = file.readlines()
#
# print(type(lines), lines, len(lines))
#
# sample_file = open(r'C:\Users\david\PycharmProjects\Python_Intro\file_test.txt')
#
# print(sample_file)
#
# file.close()
# sample_file.close()
#
# print(file.closed, sample_file.closed)
#
# with open('file_test.txt') as sample_file:
#     sample_date = sample_file.read()
# print(sample_date)
#
# with open("file_test.txt", mode="a") as sample_file:
#     sample_file.write("\nEric;151546")
#
# with open('file_test.txt', mode="r") as sample_file:
#     sample_date = sample_file.read()
#     print(sample_date)
#
# with open('file_test.txt', mode="r+") as sample_file:
#     sample_file.seek(0, 2)
#     sample_file.write("\nEric;151546")
#     sample_file.seek(0)
#     print(sample_file.read())
#
# with open('file_test2.txt', mode="w+") as sample_file:
#     sample_file.seek(0, 2)
#     sample_file.write("\nEric;151546")
#     sample_file.seek(0)
#     print(sample_file.read())
#
#
# ## Строки и байты: str, bytes, bytearray
#
# import sys
# print(sys.getdefaultencoding())
#
#
# print(ord('a'), chr(1214))
#
# s = 'hello'
# enc_ascii = s.encode('ascii')
# enc_utf8 = s.encode('utf8')
# enc_utf16 = s.encode('utf16')
# print(type(enc_ascii), enc_ascii, enc_utf8, enc_utf16)
#
# print(len(enc_ascii))
# print(len(enc_utf8))
# print(len(enc_utf16))
#
# str_in_bytes = b'hello'
# str_in_bytes = s.encode('utf8')
# str_in_text = 'hello'
# print(type(str_in_bytes),str_in_bytes)
# print(type(str_in_text),str_in_text)
#
# print(str_in_bytes[0])
# print(str_in_text[0])
#
# ba = bytearray(b'hello')
# ba[0] = 87
# print(ba)
#
# result = str(ba, 'utf8')
# print( result)
#
# result = str(ba)
# print(type(result), result)
#
# result = ba.decode('utf8')
# print(result)
#
# jpeg = [120, 3, 255, 0 , 100]
# with open(r'btest.bin', "w+b") as file:
#     file.write(bytes(jpeg))
# with open(r'btest.bin', 'rb' ) as file:
#     data = file.read()
#     for b in data:
#         print(int(b))
#
# x = "My name is Agent Smith"
# print(x[1]) #y
# print(x[3:16:3]) #nesgt
#
# ################# ДЗ №1
#
# # v.1
# input_str = input('Сколько кофе вы хотите ?\n')
#
# input_int = int(input_str)
# if input_int < 6:
#     print("Количество бонустных кофе : 0")
# else:
#     input_case = input_int / 6
# print("Количество бонустных кофе: " f'{input_case:.0f}')
# print("Количество бонустных кофе: " f'{int(input_case)}')
# print("Количество бонустных кофе: " f'{round(input_case, 0)}')
#
#
#  # v.2
# input_str = int(input('Сколько кофе вы хотите ?\n'))
# result = int(input_str / 6)
# print(result)
#
#  # v.3
# print(int(int(input('Сколько кофе вы хотите ?\n')) / 6))
#
# ################# №2
#
#
# dot_1_x = float(input('Введите x первой точки'))
# dot_1_y = float(input('Введите y первой точки'))
# dot_2_x = float(input('Введите x второй точки'))
# dot_2_y = float(input('Введите y второй точки'))
#
# # v1
# distance = ((dot_1_x - dot_2_x) ** 2 + (dot_1_y - dot_2_y) ** 2) ** 0.5
# print(f'{distance:.3f}')
# print(round(distance,3))
#
# # v2
# print(f'{((dot_1_x - dot_2_x) ** 2 + (dot_1_y - dot_2_y) ** 2) ** 0.5:.3f}')
# print(round(((dot_1_x - dot_2_x) ** 2 + (dot_1_y - dot_2_y) ** 2) ** 0.5, 3))
#
#
# ################# №3
#
#
#
# input_chicken = int(input("Введите количество куриц:\n"))
# input_swine = int(input("Введите количество свиней:\n"))
# input_cow = int(input("Введите количество коров:\n"))
#
# result = input_chicken * 2 + (input_swine + input_cow) * 4
# print(result)
