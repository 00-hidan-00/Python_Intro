# 1.

"""
Дан непустой массив целых чисел (X).
В этой задаче вам нужно вернуть массив, состоящий только из неуникальных элементов данного массива.
Для этого необходимо удалить все уникальные элементы (которые присутствуют в данном массиве только один раз).
Для решения этой задачи не меняйте оригинальный порядок элементов.
Пример: [1, 2, 3, 1, 3], где 1 и 3 неуникальные элементы и результат будет [1, 3, 1, 3].
"""
# data = [10, 9, 10, 10, 9, 8]

# def checkio(data):
#     return [x for x in data if data.count(x)>1]

# +++ my

# def checkio(data: list) -> list:
#     data_copy=data.copy()
#     [data.remove(data_copy[index]) if data_copy.count(i) == 1 else None for index, i in enumerate(data_copy)]
#     #replace this for solution
#     return data

#############################################################

# 2.

# Дана строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "start 5 one two three 7 end" есть три слова подряд.

# def checkio(words):
#     succ = 0
#     for word in words.split():
#         succ = (succ + 1)*word.isalpha()
#         if succ == 3: return True
#     else: return False

# +++

# checkio=lambda x:"www" in "".join('dw'[w.isalpha()] for w in x.split())

# +++ my

# def checkio(words: str) -> bool:
#     new_data = words.split()
#     if len(new_data) <= 2:
#         my_answer = False
#     else:
#         for index, i in enumerate(new_data[1:-1]):
#             if new_data[1:][index - 1].isalpha() and new_data[1:][index].isalpha() and new_data[1:][
#                 index + 1].isalpha():
#                 my_answer = True
#                 break
#             else:
#                 my_answer = False
#     return my_answer


# ...