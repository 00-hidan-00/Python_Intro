# генератор списков    ( list comprehension )         !!!!!!!!!!!!!!!!
#множества       ( тип )


##########################################
my_str = "qwerty"

my_list = []
for symbol in my_str:
    my_list.append(symbol)

my_list = [symbol for symbol in my_str]

print(my_list)

##########################################

limit_value = 5
numbers = [number for  number in range(limit_value)]
print(numbers)

limit_value = 5
numbers = [number **2 for  number in range(limit_value)]
print(numbers)

##########################################


my_list = [12, 32, 532, -321, 2, 0 , -12, -53]

result = [value for value in my_list if value >= 0]
print(result)

result = [value for value in my_list if type(value) == int ]   # к домашке :)
print(result)

##########################################

alphabet = [chr(index) for index in range(ord('a'),ord('z') + 1)]
print(alphabet)

my_list = list('qwerty123ytrewq321')
my_set = set(my_list)       # нет повтора, не сохраняет порядок, изменяемый
print(my_set, type(my_set))

my_str="bla BLA car"
# my_str = my_str.lower()
result =len(set(my_str.lower()))
print(result)



my_list = [1, 2, 3, 2, 2, 3]
print(set(my_list))

my_set_1 = set('12345')
my_set_2 = {"1",2,"3"}
print(my_set_1)
print(my_set_2)

##########################################

# операции с множествами

my_set_1 = set('12345')
my_set_2 = {"1",2,"3"}
result_union = my_set_1.union(my_set_2)             # объединение
print(result_union)

result_intersection = my_set_1.intersection(my_set_2)   # пересиченик
print(result_intersection)

result_difference = my_set_1.difference(my_set_2)   # разница ( вычетание )
print(result_difference)


my_str = 'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqa'

for symbol in set(my_str):
    print(symbol)


 # !  подсказка к дз !!!!!!!!!!!! ( 11 )