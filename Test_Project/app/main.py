import abc

from Test_Project.models import Human, Animal


class SomeClass(abc.ABC):
    @abc.abstractmethod
    def speak(self) -> str:
        ...


def main_function():
    human = Human(name='Gleb', age=12)
    print(human.speak())

    human_2 = Human.from_config(config={'name': "Sergej", 'age': 20})
    animal = Animal(name='GaGrrifis', age=3212)
    print(animal.speak())
    print(human_2.speak())


    # import sys
    # temp = sys.path
    # print(temp)

    # print(human._phone_number)

