# items = [1, 1, 5, 6, 7]
# border = 3
# from typing import Iterable
#
#
# def remove_all_before(items: list, border: int) -> Iterable:
#     try:
#         return items[items.index(border):]
#     except ValueError:
#         return items
#
#
# print(remove_all_before(items, border))
items_2 = [7, 7, 7, 7, 7, 7, 7, 7, 7]
border_2 = 7
result = items_2[items_2.index(border_2):] if border_2 in items_2 else items_2
print(result)

