######################## разбор ДЗ калькулятор #######################
input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n: ")

if input_case in "1234":
    try:
        value_1 = float(input("Ведите первое число:"))
        value_2 = float(input("Ведите второе число:"))
        if input_case == "1":
            result = value_1 + value_2
            sign = '+'
        elif input_case == "2":
            result = value_1 - value_2
            sign = '-'
        elif input_case == "3":
            result = value_1 * value_2
            sign = '*'
        else:
            result = value_1 / value_2
            sign = '/'
        print(f'{value_1} {sign} {value_2} = {result}')
    except ZeroDivisionError:
        print("На ноль делить нельзя, повторите еще раз")
    except ValueError:
        print("Это не число, попробуйте еще раз")
else:
    print("Вы не выбрали операцию, повторите еще раз")

