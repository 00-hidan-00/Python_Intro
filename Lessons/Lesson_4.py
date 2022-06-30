#####################################################

# or, and, not
# while
# тернарный оператор
# str

#####################################################

# or, and, not


coffe = True
tea = False

resoult = coffe and tea

print(resoult)



coffe = False
tea = False

resoult = coffe or tea

print(resoult)



coffe = False
tea = False

value = not coffe

print(value)



value = 12

if value % 2 == 0 and value % 3 == 0:
    print(f"{value} делится на 6")

# if value == True  -  плохая практика
# if value:  -  это хорошая практика



value = 12

if not value % 2 and not value % 3:
    print(f"{value} делится на 6")



value = "*"
if (value == "*") or (value == "+"):
    print("!!!")
else:
    print("???")

#####################################################

# while

value = 10

while value > 0:
    print(value)
    # value = value - 1 тоже что и  value -= 1 - уменьшение на 1
    value -= 1



value = 10

while True:
    print(value)
    value -= 1
    if value <= 0:
        break    # разрыв цикла



value = 10

go_loop = True

while go_loop:
    print(value)
    value -= 1
    if value <= 0:
        go_loop = False

#####################################################

# тернарный оператор

number = 10

if number >= 0:
    result = number ** 0.5
else:
    result = -1

print(result)



number = 10

result = number ** 0.5 if number >= 0 else -1

print(result)

#####################################################

# str

my_str = "wqfjeg2g920332jtg54c2uu690439tj432c02k309x2t6"

index = -5
symbol = my_str[index]

print(symbol)



my_str = "wqfjeg2g920332jtg54c2uu690439tj432cqf332f02k309x2t6"
print(len(my_str))



my_str = "wqfjeg2g920332jtg54c2uu690439tj432cqf332f02k309x2t6"
index = 40
if index < len(my_str):
    print(my_str[index])



# срез

my_str = "qwerty"
result = my_str[1:5]    # срез  [старт:финиш(не включен):шаг (вырез по шагу)
result = my_str[-4:-1]
result = my_str[:-1]
result = my_str[:]    # копия строки
result = my_str[3:100]
result = my_str[1:5:2]
result = my_str[::-1]  # разварот строки
result = my_str[::2]  # на четких индексах (местах)
result = my_str[1::2]  # на нечетких индексах (местах)
print(result)



value = -123

my_str = str(value) if value > 0 else str(value)[::-1]
print(my_str)