input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n")

if input_case == '1':
    value_1 = input("Введи первое число:")
    value_2 = input("Введи второе число:")
    try:
        float_value_1 = float(value_1)
        float_value_2 = float(value_2)
        result = float_value_1 + float_value_2
        print("Ответ: ", result)
    except ValueError:
        print('Это не похоже на цирфы :(')

elif input_case == '2':
    value_1 = input("Введи первое число:")
    value_2 = input("Введи второе число:")
    try:
        float_value_1 = float(value_1)
        float_value_2 = float(value_2)
        result = float_value_1 - float_value_2
        print("Ответ: ", result)
    except ValueError:
        print('Это не похоже на цирфы :(')

elif input_case == '3':
    value_1 = input("Введи первое число:")
    value_2 = input("Введи второе число:")
    try:
        float_value_1 = float(value_1)
        float_value_2 = float(value_2)
        result = float_value_1 * float_value_2
        print("Ответ: ", result)
    except ValueError:
        print('Это не похоже на цирфы :(')

elif input_case == '4':
    value_1 = input("Введи первое число:")
    value_2 = input("Введи второе число (ТОЛЬКО НЕ НОЛЬ!)")
    try:
        float_value_1 = float(value_1)
        float_value_2 = float(value_2)
        result = float_value_1 / float_value_2
        print("Ответ: ", result)
    except ValueError:
        print('Это не похоже на цирфы :(')
    except ZeroDivisionError:
        print('Ну я же просил...\nДелить на ноль нельзя!' )

elif input_case != ('1', '2', '3', '4'):
    print("Пожалуйста, выберете ОДИН из четырех вариантов !")

else:
    print("Как ты это сделал ???...")
