# тернарный оператор          !!!!!!!!!!!!!!!!!

number = 10

result = number ** 0.5 if number >= 0 else -1
print(result)

number = 10

result = number ** 0.5 if number >= 0 else -1

print(result)

##################################################################

# генератор списков            !!!!!!!!!!!!!!!!

my_str = "qwerty"

my_list = list(my_str)
my_list = list(my_str)

print(my_list)

##################################################################

# генератор словарей            !!!!!!!!!!!!!!!!

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# double_dict1={}

# for (k, v) in dict1.items():
#     double_dict1[k] = v * 2

# Удвоить каждое значение в словаре
double_dict1 = {k: v * 2 for (k, v) in dict1.items()}

print(double_dict1)


# +++

numbers = range(10)
# new_dict_for = {}

# Добавляем значения в `new_dict` с помощью цикла for
# for n in numbers:
#     if n%2==0:
#         new_dict_for[n] = n**2



# # Используем генератор словаря
new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}

##################################################################

# разрезает список и собирает обратно !!!!

my_str = 'qwerty'  # склейка строки !!!
my_list = list(my_str)
print(my_list)
new_str = " ".join(my_str)
print(new_str)

my_list = ['tmp', 'home', 'images', 'photo.png']

# метод .join работает только со списками в которых только строки !!!!
new_str = "/".join(my_list)
print(new_str)

file_path = 'home/zva/Pycharm/PythonIntro_14_03_22/lesson_6.py'

# .split разрезает все (без параметра), с параметром разрезает количество, .rsplit делает все тоже самое только с обратной стороны
parts = file_path.split('/',
                        2)
print(parts)
parts[-1] = 'to_test_dir.txt'
file_path = "/".join(parts)
print(file_path)

file_path = 'home/zva/Pycharm/PythonIntro_14_03_22/lesson_6.py'
parts = file_path.rsplit('lesson_')
print(parts)

##################################################################
