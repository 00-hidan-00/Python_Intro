# работа с файлами
# модуль os


filename = "test.py"

my_file = open(filename, 'r')   # 'r', 'w',  'rb', 'wb', ...
data = my_file.read()
my_file.close()
print(data)

with open(filename, 'r') as my_file:
    # data = my_file.read()
    # data = my_file.readline()
     data = my_file.readlines()


print(type(data))
print(data)

data.append('#TEST TEXT \n')

with open(filename.replace('.py', '_2.py'), 'w') as txt_file:
    txt_file.writelines(data)




with open(filename, 'r') as my_file:
    data = my_file.read()

data = data.split('\n')
data.append('#TEST TEXT \n')
data = '\n'.join(data)

with open(filename.replace('.py', '_2.py'), 'w') as txt_file:
    txt_file.writelines(data)