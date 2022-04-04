# tuple - картеж
# list - список

my_tuple = (1, 2, 3, "qwerty", True, None, 'tuple')  # неизменяемый объект

my_list = [1, 2, 3, "qwerty", True, None, 'list']  # изменяемый объект

print(type(my_tuple), type(my_list))


##################################################################

# итерируемые объекты  ( и tuple, и list )

print(my_tuple[2:])

new_tuple = tuple(my_list)
print(new_tuple)

##################################################################

new_lsit = list()
print(new_lsit)

new_tuple = tuple()
print(new_tuple)

new_lsit = list("qwert")
new_lsit = ['qwerty',
            12,
            123
            ]
print(new_lsit)

new_tuple = tuple("qwerty")
new_tuple = ('qwerty',
             322,
             21
             )
print(new_tuple)

new_lsit = ["15.325.643.36.1",
            "15.325.643.36.1",
            "15.325.643.36.1",
            ]
print(new_lsit)

##################################################################   !!!
base_list = [1, 2, 3]
my_new_list = base_list * 4


base_list[0] = 10
print(f'{base_list=}')
print(f'{my_new_list}')
##################################################################   !!!
base_list = [1,2,3]
new_list = [base_list.copy()] * 5

base_list[0] = 10
print(f'{base_list=}')
print(f'{new_list=}')
##################################################################

my_tuple = (1, 2, 3, "qwerty", True, None, ['tuple'])

my_list = [1, 2, 3, "qwerty", True, None, ['list']]


value = "10"
my_list[-1][0] = value
print(my_list)

value = "10"
my_tuple[-1][0] = value
print(my_tuple)

##################################################################

my_lsit = []
if my_lsit:
    value = my_lsit[0]
    print(value)


########### как нужно делать (ниже)
my_list = [1, 2, 3,]
index_value = 4
value = 100

if len(my_list) > index_value:
    value = my_list[index_value]
print(value)


########### так не нужно делать (ниже)
try:
    value = my_list[index_value]
    print(value)
except IndexError:
    pass
print(value)

##################################################################

my_list = []
my_str = 'qwerty'

# my_list.append(21)   # добавление элемента в конце списка

for simbol in my_str:       # объект с тем же id (наполнили предыдущий)
    my_list.append(simbol)

# my_list = list(my_str)    # объект с новым id
print(my_list)



del_value = my_list.pop()   # уберает элемента в конце списка (может по номеру в списке)
print(my_list, del_value)

##################################################################

my_str = 'qwerty'     # склейка строки !!!
my_list = list(my_str)
print(my_list)
new_str = " ".join(my_str)
print(new_str)

my_list = ['tmp', 'home', 'images', 'photo.png']
new_str = "/".join(my_list)      #  метод .join работает только со списками в которых только строки !!!!
print(new_str)



file_path = 'home/zva/Pycharm/PythonIntro_14_03_22/lesson_6.py'
parts = file_path.split('/', 2)    # .split разрезает все (без параметра), с параметром разрезает количество, .rsplit делает все тоже самое только с обратной стороны
print(parts)
parts[-1] = 'test.txt'
file_path = "/".join(parts)
print(file_path)



file_path = 'home/zva/Pycharm/PythonIntro_14_03_22/lesson_6.py'
parts = file_path.rsplit('lesson_')
print(parts)


##################################################################

#сортировка

my_list = [2, 5, 1, 9, -4, 7]
my_list = ['tmp', 'home', 'Images', 'photo.png', '123', '@', '"', '[']

my_list.sort()  #  сортирует текущий список БЕЗ возможности вернуть старый порядок
print(my_list)

sort_list = sorted(my_list)  # сортирует копию списка
print(sort_list, my_list)

sort_list = sorted(my_list, reverse=True)  # сортирует список наоборот
print(sort_list)

sort_list = sorted(my_list, key=abs)  # сортирует список без учета знака минус
print(sort_list)

sort_list = sorted(my_list, key=len)  # сортирует список по количеству знаков
print(sort_list)

# ASCII - таблица символов

print(ord('1'))

print(chr(103))