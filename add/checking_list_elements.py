# Проверка уникальности элементов списка

from random import randrange

N = 10
arr = [randrange(50) for i in range(N)]
print(*arr, type(arr))


if len(set(arr)) == len(arr):
    print("Все элементы индивидуальны")
else:
    print("Есть одинаковые")

#############################################

def unique(lst: list) -> bool:
    for i in range(N - 1):
        for j in range(i + 1, N):
            if lst[i] == lst[j]:
                return False
    return True

#############################################

def unique(lst: list) -> bool:
    for i in lst:
        if lst.count(i) > 1:
            return False
    return True


#############################################

if unique(arr):
    print("Все элементы индивидуальны")
else:
    print("Есть одинаковые")
