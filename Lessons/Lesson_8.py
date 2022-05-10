# словари и методы словарей
# распаковка кортежей и списков
######################################
### словари и методы словарей

my_dict = {'key': 'value'}   # ключ - любой НЕИЗМЕНЯЕМЫЙ ОБЪЕКТ
                             # значение - любой объект
print(my_dict, type(my_dict))

######################################

address = {'city': 'Dnipro',
           'street': 'Polya',
           'zip': 49000
           }

person = {'name': 'John',
          'age': 24,
          'job': 'president',
          'address': address  # двух уровневый доступ к данным
          }

print(person['age'])
print(person['address']['city'])

test_dict = {1: 'to_test_dir',
             2.3: 'test_2',
             (1, 2): 1000,
             # [1,2]: 'to_test_dir'          # спосок в словаре не может быть ! ( ток не изменяемые)
             (tuple([1, 2]), 1): 'to_test_dir'
             }

print(test_dict[tuple([1, 2]), 1])

######################################

from random import randint

cube_dict = {
    1: 'this is 1',
    2: 'this is 2',
    3: 'this is 3',
    4: 'this is 4',
    5: 'this is 5',
    6: 'this is 6'
}

value = randint(1, 100)

my_result = cube_dict[value % 6]
print(value, my_result)

######################################

test_dict = dict()
test_dict['new_key'] = 100
test_dict.update({'to_test_dir': 'value'})     # добавление ( может перезаписать )

my_dict = {'to_test_dir': 'value',
           'test_2': '1'}     # создание
test_dict.update(my_dict)

get_value = test_dict.get('new_key')
get_value_2 = test_dict['new_key']
разница
get_value = test_dict.get('key', -1)    # НЕ получим ошибку
get_value_2 = test_dict['key']      # получим ошибку

pop_value = test_dict.pop('to_test_dir')      # возвращает/удаляет часть словаря по ключу
print(pop_value)

######################################

address = {'city': 'Dnipro',
           'street': 'Polya',
           'zip': 49000
           }

address['district'] = 'center'  # добавление
address['zip'] = '48022'  # замена
print(address)

######################################

address = {'city': 'Dnipro',
           'street': 'Polya',
           'zip': 49000
           }

key = 'key'
if key in address:  # in мотрит в ключи !!!
    get_value = address[key]
    print(get_value)
else:
    address[key] = None


for key in address.keys():
    print(key, address[key])     # по ключу получить значение МОЖНО, наоборот НЕТ !!!

print(list(address.keys()))     # собирает ключи

print(list(address.values()))     # собирает значения

values = list(address.values())
values.append(5)
print(values)

for value in address.values():   # !!!!
    print(value)

items = address.items()
print(items)
print(list(items))

for key, value in address.items():       # самый
    print(key, value)

######################################

ascii_dict = {}
for key in range(80, 100):
    ascii_dict[key] = chr(key)
print(ascii_dict)

ascii_dict = {key:chr(key) for key in range(50, 61)}
print(ascii_dict)

######################################

ascii_dict_value = {}
for key, value in ascii_dict.items():
    ascii_dict_value[value] = key
print(ascii_dict_value)

ascii_dict_value = {value:key for key, value in ascii_dict.items()}
print(ascii_dict_value)
######################################

price_list = [{"product": "MacBook", "price": 32000, "brand": "Apple"},
              {"product": "MacBookPro", "price": 52000, "brand": "Apple"},
              {"product": "HP", "price": 15000, "brand": "HP"}]

prices = []

for notebook in price_list:
    prices.append(notebook['price'])
average_price = sum(prices) / len(prices)
print(average_price)

######################################
### словари и методы словарей
######################################

my_tuple = (1, 2, 'ok')
value_1, value_2, my_str = my_tuple

print(value_2, my_str)

######################################

value_1 = 2
value_2 = 4
value_1, value_2 = value_2, value_1
print(value_1, value_2)

# объяснение процесса переменной

tmp = value_1, value_2
print(tmp)
value_2, value_1 = tmp

######################################

my_tuple = (1, 2, 'ok', 'to_test_dir', 200)

value_1, value_2 = my_tuple[:2]
print(my_tuple)

value_1, value_2, _, _ = my_tuple
print(my_tuple, _)

value_1, value_2, *tmp, last_value = my_tuple   # звездрчкой собрать остатки
print(tmp)

value_1, value_2, *_, last_value = my_tuple   # обычно звездочку используют для заглушки
print(_)

print(my_tuple)
print(*my_tuple)
