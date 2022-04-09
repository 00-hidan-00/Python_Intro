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


python = 'Pyrhon is fun'            # Возвращает кортеж, содержащий часть перед первым шаблоном, сам шаблон, и часть после шаблона. Если шаблон не найден, возвращается кортеж, содержащий саму строку, а затем две пустых строки
print(python.partition('is '))
print(python.partition('not '))
python = "Pyrhon is fun, isn't it"
print(python.partition('is'))