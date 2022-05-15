# полиморфизм

# class BBox:
#     def __init__(self, x0, y0, x1, y1):
#         self._x0 = x0
#         self._y0 = y0
#         self._x1 = x1
#         self._y1 = y1
#
#     def __repr__(self):
#         return f"({self._x0}; {self._y0}) - ({self._x1}; {self._y1})"
#
#     def get_area(self):
#         return (self._x1 - self._x0) * (self._y1 - self._y0)
#
#     def __add__(self, other):
#         new_x0 = min(self._x0, other._x0)
#         new_y0 = min(self._y0, other._y0)
#         new_x1 = max(self._x1, other._x1)
#         new_y1 = max(self._y1, other._y1)
#         return BBox(new_x0, new_y0, new_x1, new_y1)
#
#
# bbox_1 = BBox(0, 0, 3, 4)
# bbox_2 = BBox(1, 2, 5, 5)
#
# bbox_3 = bbox_1 > bbox_2
#
# print(bbox_3)


