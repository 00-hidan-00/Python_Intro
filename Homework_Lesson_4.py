#   # 1) У вас есть переменная value, тип - int.
#   Написать тернарный оператор для переменной new_value по такому правилу: если value меньше 100, то new_value равно половине значения value,
#   в противном случае - противоположне value число

# value = 100
#
# new_value = value / 2 if value < 100 else value * -1
#
# print(new_value)



#   # 2) У вас есть переменная value, тип - int.
#   Написать тернарный оператор для переменной new_value по такому правилу: если value меньше 100, то new_value равно 1, в противном случае - 0

# value = 100
#
# new_value = value = 1 if value < 100 else value * 0
#
# print(new_value)



#   # 3) У вас есть переменная value, тип - int.
#   Написать тернарный оператор для переменной new_value по такому правилу: если value меньше 100, то new_value равно True, в противном случае - False

# value = 0
#
# new_value = True if value < 100 else False
#
# print(new_value)



#   4) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки себя же.
#   Пример: было - "qwer", стало - "qwerqwer". Если длинна не меньше 5, то оставить строку как есть.

# my_str = "123123"
#
# my_str = my_str * 2 if len(my_str) < 5 else my_str
#
# print(my_str)



# 5) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки перевернутую себя же.
# Пример: было - "qwer", стало - "qwerrewq". Если длинна не меньше 5, то оставить строку как есть.

# my_str = "123"
#
# my_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
#
# print(my_str)


# 6) Доработать задание с калькулятором, чтобы в конце вычисления у пользователя спрашивало, нужен ли калькулятор еще.
# И если да, то запустить вычисление заново




# В самом низу есро вопрос
go_loop = True

while go_loop:
    input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n")

    if input_case == '1':
        value_1 = input("Введи первое число:\n")
        value_2 = input("Введи второе число:\n")
        try:
            float_value_1 = float(value_1)
            float_value_2 = float(value_2)
            result = float_value_1 + float_value_2
            print("Ответ: ", result)
        except ValueError:
            print('Это не похоже на цирфы :(\nПридётся начать с начала...')

    elif input_case == '2':
        value_1 = input("Введи первое число:\n")
        value_2 = input("Введи второе число:\n")
        try:
            float_value_1 = float(value_1)
            float_value_2 = float(value_2)
            result = float_value_1 - float_value_2
            print("Ответ: ", result)
        except ValueError:
            print('Это не похоже на цирфы :(\nПридётся начать с начала...')

    elif input_case == '3':
        value_1 = input("Введи первое число:\n")
        value_2 = input("Введи второе число:\n")
        try:
            float_value_1 = float(value_1)
            float_value_2 = float(value_2)
            result = float_value_1 * float_value_2
            print("Ответ: ", result)
        except ValueError:
            print('Это не похоже на цирфы :(\nПридётся начать с начала...')

    elif input_case == '4':
        value_1 = input("Введи первое число:\n")
        value_2 = input("Введи второе число (ТОЛЬКО НЕ НОЛЬ!)\n")
        try:
            float_value_1 = float(value_1)
            float_value_2 = float(value_2)
            result = float_value_1 / float_value_2
            print("Ответ: ", result)
        except ValueError:
            print('Это не похоже на цирфы :(\nПридётся начать с начала...')
        except ZeroDivisionError:
            print('Ну я же просил...\nДелить на ноль нельзя!' )
    elif input_case != ('1', '2', '3', '4'):
        print("Пожалуйста, выберете ОДИН из четырех вариантов !\nПридётся начать с начала...")
    else:
        print("Как ты это сделал ???...")



    continue_request_loop = True
    while continue_request_loop:
        continue_request = input('\nЧто бы продолжить введите "y"\nЧто бы прекратить введите "n"\n')
        if continue_request == "n":
            # Объясните пожалуйста !
            # Как тут можно задать больше значений ? Например ("n", "N", "No"),
            # <<<if continue_request == ("n", "N", "Not")>>> не рабоатет, хотя тут  <<<elif continue_request != ('n', 'y')>>> все идет
            # Заранее спасибо за ответ !
            continue_request_loop = False
            go_loop = False
        elif continue_request == "y":
            continue_request_loop = False
        elif continue_request != ('n', 'y'):
            print("Следуйте инструкции !")
