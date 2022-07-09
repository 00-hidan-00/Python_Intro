# https://pythonru.com/primery/primery-raboty-s-klassami-v-python

class Employee:
    """Базовый класс для всех сотрудников"""

    # Переменная emp_count — переменная класса, значение которой разделяется между экземплярами этого класса.
    emp_count = 0  #

    # Первый метод __init__() — специальный метод, который называют конструктором класса или методом инициализации.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        # Получить доступ к этой переменной можно через Employee.emp_count из класса или за его пределами.
        Employee.emp_count += 1

    def display_count(self):
        print('Всего сотрудников: %d' % Employee.emp_count)

    def display_employee(self):
        print(f'Имя: {self.name}. Зарплата: {self.salary}')


# Это создаст первый объект класса Employee
emp1 = Employee("Андрей", 2000)
# Это создаст второй объект класса Employee
emp2 = Employee("Мария", 5000)
emp1.display_employee()
emp2.display_employee()
print("Всего сотрудников: %d" % Employee.emp_count)

# getattr(obj, name [, default]) — для доступа к атрибуту объекта.
# hasattr(obj, name) — проверить, есть ли в obj атрибут name.
# setattr(obj, name, value) — задать атрибут. Если атрибут не существует, он будет создан.
# delattr(obj, name) — удалить атрибут.

# print(hasattr(emp1, "name") )

###

# print("Employee.__doc__:", Employee.__doc__)
# print("Employee.__name__:", Employee.__name__)
# print("Employee.__module__:", Employee.__module__)
# print("Employee.__bases__:", Employee.__bases__)
# print("Employee.__dict__:", Employee.__dict__)

# __dict__ — словарь, содержащий пространство имен класса.
# __doc__ — строка документации класса. None если, документация отсутствует.
# __name__ — имя класса.
# __module__ — имя модуля, в котором определяется класс. Этот атрибут __main__ в интерактивном режиме.
# __bases__ — могут быть пустые tuple, содержащие базовые классы, в порядке их появления в списке базового класса.

###

a = 40  # создали объект <40>
b = a  # увеличивает количество ссылок  <40>
c = [b]  # увеличивает количество ссылок <40>

del a  # уменьшает количество ссылок <40>
b = 100  # уменьшает количество ссылок <40>
c[0] = -1  # уменьшает количество ссылок <40>


###

# Пример наследования класса в Python

class Parent:  # объявляем родительский класс
    parent_attr = 100

    def __init__(self):
        print('Вызов родительского конструктора')

    def parent_method(self):
        print('Вызов родительского метода')

    def set_attr(self, attr):
        Parent.parent_attr = attr

    def get_attr(self):
        print(f'Атрибут родителя: {Parent.parent_attr}')


class Child(Parent):  # объявляем класс наследник
    def __init__(self):
        print('Вызов конструктора класса наследника')

    def child_method(self):
        print('Вызов метода класса наследника')


# c = Child()  # экземпляр класса Child
# c.child_method()  # вызов метода child_method
# c.parent_method()  # вызов родительского метода parent_method
# c.set_attr(200)  # еще раз вызов родительского метода
# c.get_attr()  # снова вызов родительского метода

###

# Переопределение методов

class Parent:  # объявите родительский класс
    def my_method(self):
        print('Вызов родительского метода')


class Child(Parent):  # объявите класс наследник
    def my_method(self):
        print('Вызов метода наследника')


c = Child()  # экземпляр класса Child
c.my_method()  # метод переопределен классом наследником


#

# Популярные базовые методы
# В данной таблице перечислены некоторые общие функции. Вы можете переопределить их в своих собственных классах.
#
# №	Метод, описание и пример вызова
# 1	__init__(self [, args...]) — конструктор (с любыми необязательными аргументами)
# obj = className(args)
# 2	__del__(self) — деструктор, удаляет объект
# del obj
# 3	__repr__(self) — программное представление объекта
# repr(obj)
# 4	__str__(self) — строковое представление объекта
# str(obj)

# Пример использования __add__

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector ({}, {})'.format(self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)


###

# Приватные методы и атрибуты

class JustCounter:
    __secret_count = 0

    def count(self):
        self.__secret_count += 1
        print(self.__secret_count)


counter = JustCounter()
counter.count()
counter.count()
# print(counter.__secret_count)


##############

class Car:
    def __init__(self, color: str, mileage: int):
        self.color = color
        self.mileage = mileage


blue_car = Car(color='blue', mileage=20000)
red_car = Car(color='rad', mileage=30000)

for car in (blue_car, red_car):
    print(f"The {car.color} car has {car.mileage:,} miles")


###


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)


class Dachshund(Dog):
    pass


class Bulldog(Dog):
    pass


miles = Dog("Miles", 4)
buddy = Dog("Buddy", 9)
jack = Dog("Jack", 3)
jim = Dog("Jim", 5)

miles = JackRussellTerrier("Miles", 4)

print(miles.speak("Grrr"))

jim = Bulldog("Jim", 5)

print(jim.speak("Woof"))

miles = JackRussellTerrier("Miles", 4)
print(miles.speak())

###

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound = "Bark"):
        return super().speak(sound)


my_dog = GoldenRetriever("Granata", 4)

print(my_dog.speak())

import platform
print(platform.python_implementation())