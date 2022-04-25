###   Calculator version 1   ####


# input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n")
#
# if input_case == '1':
#     value_1 = input("Введи первое число:")
#     value_2 = input("Введи второе число:")
#     try:
#         float_value_1 = float(value_1)
#         float_value_2 = float(value_2)
#         result = float_value_1 + float_value_2
#         print("Ответ: ", result)
#     except ValueError:
#         print('Это не похоже на цирфы :(')
#
# elif input_case == '2':
#     value_1 = input("Введи первое число:")
#     value_2 = input("Введи второе число:")
#     try:
#         float_value_1 = float(value_1)
#         float_value_2 = float(value_2)
#         result = float_value_1 - float_value_2
#         print("Ответ: ", result)
#     except ValueError:
#         print('Это не похоже на цирфы :(')
#
# elif input_case == '3':
#     value_1 = input("Введи первое число:")
#     value_2 = input("Введи второе число:")
#     try:
#         float_value_1 = float(value_1)
#         float_value_2 = float(value_2)
#         result = float_value_1 * float_value_2
#         print("Ответ: ", result)
#     except ValueError:
#         print('Это не похоже на цирфы :(')
#
# elif input_case == '4':
#     value_1 = input("Введи первое число:")
#     value_2 = input("Введи второе число (ТОЛЬКО НЕ НОЛЬ!)")
#     try:
#         float_value_1 = float(value_1)
#         float_value_2 = float(value_2)
#         result = float_value_1 / float_value_2
#         print("Ответ: ", result)
#     except ValueError:
#         print('Это не похоже на цирфы :(')
#     except ZeroDivisionError:
#         print('Ну я же просил...\nДелить на ноль нельзя!' )
#
# elif input_case != ('1', '2', '3', '4'):
#     print("Пожалуйста, выберете ОДИН из четырех вариантов !")
# else:
#     print("Как ты это сделал ???...")


##   Calculator version 2   ####

input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n")
if input_case in "1234":
    try:
        value_1 = float(input("Введи первое число:"))
        value_2 = float(input("Введи второе число:"))
        if input_case == '1':
            result = value_1 + value_2
            sign = '+'
        elif input_case == '2':
            result = value_1 - value_2
            sign = '-'
        elif input_case == '3':
            result = value_1 * value_2
            sign = '*'
        elif input_case == '4':
            result = value_1 / value_2
            sign = '/'
        print(f'{value_1} {sign} {value_2} = {result}')
    except ValueError:
        print('Это не похоже на цирфы :(')
    except ZeroDivisionError:
        print('Ну я же просил...\nДелить на ноль нельзя!')
else:
    print("Пожалуйста, выберете ОДИН из четырех вариантов !")
