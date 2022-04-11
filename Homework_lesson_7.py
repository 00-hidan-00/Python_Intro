# 1. Дано целое число (int). Определить сколько нулей в этом числе.

my_int = 100

my_number = 0
my_int_str = str(my_int)
my_number_str = str(my_number)
result = my_int_str.count(my_number_str)
print(result)


# result = str(my_int).count(str(my_number))
# print(result)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля

# v1.0
my_int = 10022150000
box = ''
# box = []
my_int_str = str(my_int)
for index in my_int_str[::-1]:
    box += index
    # box.append(index)
    result = len(box) - 1
    if index != "0":
        break

print(result)


# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1 = [1,2,1,2,1,2]
my_list_2 = [3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4]
my_result = []

# v1.0
for index in my_list_1[::2], my_list_2[1::2]:
    my_result += index
print(my_result)

# V2.0
# my_result += [index for index in my_list_1[::2] + my_list_2[1::2]]

print(my_result)


# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list = [1,2,3,4]
new_list = [index for index in my_list[::-1]]

print(new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

# V1
my_list = [1, 2, 3, 4, 5]
print(id(my_list))

# V1a
index_1 = my_list.pop(0)
my_list.insert(-1, index_1)
index_2 = my_list.pop(-1)
my_list.insert(0, index_2)

# V1b
# my_list.insert(-1, my_list.pop(0))
# my_list.insert(0, my_list.pop(-1))

print(my_list, id(my_list))

# V2
my_list = [1, 2, 3, 4, 5]
print(id(my_list))
index_1 = my_list[0]
index_2 = my_list[-1]

my_list[-1] = index_1
my_list[0] = index_2
print(my_list, id(my_list))

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)

my_str = "43 больше чем 34 но меньше чем 56"
result = 0
my_list = my_str.split(' ')
for number in my_list:
    if number.isdigit():
        result += int(number)
print(result)


# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "My long string"
l_limit = "o"
r_limit = "g"

index_l= my_str.find(l_limit) + 1
index_r= my_str.rfind(r_limit)
sub_str = my_str[index_l:index_r]


sub_str = my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]

print(sub_str)


# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)

#не знаю как решить, дайте пожалуйста подсказку.   !!!!!!

# my_str = 'adcdad'
# my_list = list(my_str)
# box = []
# for index, symbol in enumerate(my_list):
#     box.append(my_str[:2])
#     print(box)

# for symbol in my_str:
#     my_list = symbol[0:2]
#     print(my_list)

# my_str = 'adcdad'
# my_result = []
# my_str_1 = []
# my_str_2 = []
# my_str_1 += my_str[:2]
# my_str_2 += my_str[1:3]
# print(my_str_1,my_str_2)

# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

# не знаю как решить, дайте пожалуйста подсказку.   !!!!!!

# my_list = [2,4,1,5,3,9,0,7]
# box = []
# for symbol in my_list[::2]:
#     x = my_list[:3]
#     print(x)



# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.

my_list =[1, 2, 3, "11", "22", 33]
result = [value for value in my_list if type(value) == str ]
print(result)

# 11. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.


my_str = '11222E12D11'
result = list(set(my_str))
print(result)


# 12. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str_1 = "a1234tt"
my_str_2 = "a1234rr"

result = list(set(my_str_1).intersection(set(my_str_2)))
print(result)

# 13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу


# не знаю как решить, дайте пожалуйста подсказку.   !!!!!!


# my_str_1 = "aaaasdf1"
# my_str_2 = "asdfff2"
#
# resilt = []
# for sumbol in


# list_len = max(len(my_str_1), len(my_str_2))
# for index in range(list_len):
#     value_1 = my_str_1[index]
#     value_2 = my_str_2[index]
#     resilt += [value_1, value_2]
#
#
# resilt += my_str_1[list_len:]
# resilt += my_str_2[list_len:]
#
# print(resilt)


