# debugger
# for
# str methods


######################################################

# for

# my_str = "qwerty123456"

# for symbol in my_str:
#     print(symbol)

# for symbol in my_str[:6]:
#     print(symbol)

# for index in range(5):
#     print(index)

# for index in range(len(my_str)):
#     print(index, my_str[index])

# for index, symbol in enumerate(my_str):
#     print(index, symbol)

######################################################

# str methods

# my_str = "qwerty"

# my_str_len = len(my_str)
# print(my_str_len)

# print(my_str.isalpha())


# my_str = "My name is John i'm 40"

# for symbol in my_str:
#     if not symbol.isupper():
#         print(symbol)

# for symbol in my_str:
#     if symbol.islower() and symbol.isalpha() and symbol not in "eyuioa":
#         print(symbol)

# result = my_str.find("John")
# print(result)


# filename = "images_123.png"
# filename = filename.replace('png', 'jpg')
# print(filename)



# my_str = "My name is Anna, i'm 40. It is dog"
#
# for symbol in my_str:
#     if symbol.lower() in 'eyuioa':
#         print(symbol)


# my_str = "My name is Anna, i'm 40. It is dog"
#
# print(my_str.lower().count('a'))


# my_str = "My name is Anna, i'm 40. It is dog"
#
# result = ''
# for symbol in my_str:
#     if symbol.isalpha() and symbol.islower() and symbol not in "eyuioa":
#         result += symbol
# print(result)

# filename = "images_png_123.png"
# f_name = filename[::-1].replace('gnp', 'gpj', 1)
# filename = f_name[::-1]
# print(filename)





######################## разбор ДЗ калькулятор #######################
# input_case = input("Выбери тип операции:\n1 +\n2 -\n3 *\n4 /\n: ")
#
# if input_case in "1234":
#     try:
#         value_1 = float(input("Ведите первое число:"))
#         value_2 = float(input("Ведите второе число:"))
#         if input_case == "1":
#             result = value_1 + value_2
#             sign = '+'
#         elif input_case == "2":
#             result = value_1 - value_2
#             sign = '-'
#         elif input_case == "3":
#             result = value_1 * value_2
#             sign = '*'
#         else:
#             result = value_1 / value_2
#             sign = '/'
#         print(f'{value_1} {sign} {value_2} = {result}')
#     except ZeroDivisionError:
#         print("На ноль делить нельзя, повторите еще раз")
#     except ValueError:
#         print("Это не число, попробуйте еще раз")
# else:
#     print("Вы не выбрали операцию, повторите еще раз")
