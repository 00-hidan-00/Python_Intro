import random

value = random.randint(0,4)
print(value)

my_cases = [True, False,100,'qwerty']
case = random.choice(my_cases)
print(case)

random.shuffle(my_cases)
print(my_cases)