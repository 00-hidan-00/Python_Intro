# ООП - ОБЪЕКТНО ОРИЕНТИРОВАННОЕ ПРОГРАММИРОВАНИЕ
# класс
# экземпляр класса  -  "self"
# атрибут класса
# атрибут экземпляра класса
from typing import Optional


# class Person:  # класс
#     name: Optional[str] = None
#     age: int = 0
#     job: dict = {'Title': 'Programmer',
#                  'Company': 'GoWombat'
#                  }
#
#
# person_1 = Person()  # экземпляр класса ( представитель объекта )
# person_2 = Person()
#
# person_1.name = 'John'  # атрибут экземпляра класса
# person_1.age = 23
#
# person_2.name = 'Anna'
# person_2.age = 30
# person_2.gender = 'male'  # добавили атрибут в экземпляр класса
#
# person_3 = Person()
# Person.name = 'Jack'
# person_4 = Person()
#
# print(person_1.name, person_1.age)
# print(person_2.name, person_2.age, person_2.gender)
# print(person_3.name, person_3.age)
# print(person_4.name, person_4.age, person_4.job['Company'])

#############################################################

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.name_uppercase = self.get_name_uppercase()

    def __str__(self):
        return f"""I'm {self.name}, i'm {self.age}"""

    def __repr__(self):
        return f"{self.name_uppercase}"

    def increase_age(self):
        self.age += 1

    def get_name_uppercase(self):
        name_uppercase = self.name.upper()
        return name_uppercase


my_name = "Davyd"
my_age = 21

Taranov = Person(my_name, my_age)
print(Taranov)

person_1 = Person(name='John', age=23)
print(person_1.name, person_1.age)

person_2 = Person(name='Eva', age=30)
print(person_2)

person_1.increase_age()
persons = [person_1, person_2]
print(persons)
