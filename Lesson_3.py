# тип bool, None
# привидение типов
# оператор if
# функция input
# обработка ошибок

#####################################################

# Nome

none_value = None

print(none_value, type(none_value))

value = 123
id_value = id(value)
print(id_value)

print_value = print(value)
print(print_value)

value = 123
id_value = id(value)
print(f"{id_value=}")

print_value = print("----->", value)

print(f"{print_value=}")

#####################################################

# bool

value_1 = True
value_2 = False

print(type(value_1), type(value_2))


bool_value = 4 > 2            # >, <, >=, <=, ==, !=
bool_value = "qwe" in "qwerty"


print(bool_value)

#####################################################

value_int = 12
value_float = 3.14
result = value_float + value_int
print(result)

value_int = 1

value_float = float(value_int)     # int --> float
value_str = str(value_int)         # int --> str
value_bool = bool(value_int)       # int --> bool  !!! True всегла кроме 0

print(value_float, value_str, value_bool)

#####################################################

value_float = 1.0

value_int = int(value_float)        # float --> intccv    !!! "отрезание" всего после точки
value_str = str(value_float)        # float --> str
value_bool = bool(value_float)      # float --> bool  !!! True всегла кроме 0.0

print(value_int, value_str * 3, value_bool)

#####################################################

value_str = "10"

# value_int = int(value_str)             # str --> intccv
# value_float = float(value_str)         # str --> str
#утиная типизация

value_bool = bool(value_str)           # str --> bool  !!! True всегла кроме ""

print(value_int, value_float * 3, value_bool)

#####################################################

# оператор if

# value = 12
# if условие:
#     # блок, если ДА
# elif условие 2:
#     # блок, если ДА
# else:
#     # блок, если НЕТ

value = 101
if value > 100:
    print(f"Число {value} больше чем 100")
elif value < 100:
    print(f"Число {value} меньше  100")
else:
    print(f"Число {value} равно 100" )


value = 20
if value < 0:
    print(f"Число {value} меньше 0")
elif value == 0:
    print(f"Число {value} это число 0")
elif 0 <= value < 100:
    print(f"Число {value} меньше 0, но больше 100")
elif value == 100:
    print(f"Число {value} это число 100")
elif 100 <= value < 1000:
    print(f"Число {value} меньше 100, но больше 1000")
elif value == 1000:
    print(f"Число {value} это число 1000")
else:
    print(f"Число {value} больше 1000")

#####################################################

# функция input

input_value = input("Введи целое число: ")
int_value = int(input_value)
print(int_value, type(int_value))

int_value = int(input("Введи целое число: "))
print(int_value * 10, type(int_value))

#####################################################

# обработка ошибок


input_value = input("Введи целое число: ")
try:
    int_value = int(input_value)
    print(int_value, type(int_value))
except:
    pass


input_value = input("Введи целое число: ")
try:
    int_value = int(input_value)
    print(1 / int_value * 2)
except ValueError:
    print("Это не целое число!")
except ZeroDivisionError:
    print("На 0 делить нельзя")
except (AssertionError, RuntimeError):
    print("Что-то не то")


#####################################################

# ДЗ

input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n")
value_1 = input("Введи первое число:")
value_2 = input("Введи второе число:")
if input_case == '1':
    result = value_1 + value_2
print(result)

