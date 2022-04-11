# тернарный оператор          !!!!!!!!!!!!!!!!!

number = 10

if number >= 0:
    result = number ** 0.5
else:
    result = -1

print(result)



number = 10

result = number ** 0.5 if number >= 0 else -1

print(result)

###########################


my_str = "My name is Anna, i'm 40. It is dog"

result = ''
for symbol in my_str:
    if symbol.isalpha() and symbol.islower() and symbol not in "eyuioa":
        result += symbol
print(result)


my_list = [1, 2, 3,]
index_value = 4
value = 100

if len(my_list) > index_value:
    value = my_list[index_value]
print(value)

##################################################################

# разрезает список и собирает обратно !!!!

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


# генератор списков            !!!!!!!!!!!!!!!!

my_str = "qwerty"

# my_list = []
# for symbol in my_str:
#     my_list.append(symbol)

my_list = [symbol for symbol in my_str]

print(my_list)