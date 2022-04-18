my_dict_1 = {'city': "Dnipro",
             '543': 3235,
             'street': 'Polya',
             'zip': 49000,
             '1': 2,
             "few": 124,
             }
my_dict_2 = {'name': 'John',
             "age": 24,
             'Job': 'president',
             'street': 'Polya',
             'zip': 49000,
             '1': 2,
             '2': 22,
             "few": 124,
             }

# result_2 = list(set(my_dict_1.keys()).difference(set(my_dict_2.keys())))

new_dict = {}
for key in my_dict_1:
    if key in my_dict_2:
        new_dict[key] = [my_dict_1[key], my_dict_2[key]]
    else:
        new_dict[key] = my_dict_1[key]
for key in my_dict_2:
    if key not in my_dict_1:
        new_dict[key] = my_dict_2[key]
print(new_dict)