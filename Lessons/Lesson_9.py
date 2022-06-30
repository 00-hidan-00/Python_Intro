# модули
# функции ( Lesson_9_2.py )

#####################################

### модули

import string

alphabet = ''.join([chr(idx) for idx in range(ord('a'), ord('z') + 1)])
# создали алфавит

alphabet = 'qwertyuiopasdfghjklzxcvbnm'

alphabet = string.ascii_lowercase

print(alphabet)

#####################################

## типы импортов

# 1
import string

alphabet = string.ascii_letters
print(alphabet)

# 2
from string import ascii_lowercase
alphabet = ascii_lowercase
print(alphabet)

# 3
from string import ascii_lowercase as alphabet
from string import ascii_uppercase as ALPHABET
print(alphabet, ALPHABET)

#####################################

# 1
import random

value = random.randint(0,4)
print(value)

my_cases = [True, False,100,'qwerty']
case = random.choice(my_cases)
print(case)

random.shuffle(my_cases)
print(my_cases)

# 2

from random import randint, choice, shuffle
from random import * # ООЧЕНЬ осторожно использовать

value = randint(0, 4)
print(value)

my_cases = [True, False, 100, 'qwerty']
case = choice(my_cases)
print(case)

shuffle(my_cases)
print(my_cases)
