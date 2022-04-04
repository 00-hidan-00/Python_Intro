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

my_list = []
my_str = 'qwerty'

# my_list.append(21)   # добавление элемента в конце списка

for simbol in my_str:       # объект с тем же id (наполнили предыдущий)
    my_list.append(simbol)

# my_list = list(my_str)    # объект с новым id
print(my_list)