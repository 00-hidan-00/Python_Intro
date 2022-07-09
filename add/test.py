import abc

from Test_Project.app.typing import ClassVar
from Test_Project.app.typing import T_Subjects, T_Name


class SomeClass(abc.ABC):
    @abc.abstractmethod
    def speak(self) -> str:
        ...


class Human:
    knowledge: ClassVar[T_Subjects] = []

    def __init__(self, name: T_Name, age: int):
        self.name = name
        self.age = age
        self._phone_number = None
        self.__passport_date = None

    @classmethod
    def from_config(cls, config: dict):
        return cls(**config)

    @staticmethod
    def some_method() -> int:
        return 42

    def speak(self):
        return f'i\'m {self.name}. I\'m {self.age}'


def main():
    human = Human(name='Gleb', age=12)
    print(human.speak())

    human_2 = Human.from_config(config={'name': "Sergej", 'age': 20})
    print(human_2.speak())

    # print(human._phone_number)


if __name__ == '__main__':
    main()


# F6  - перенос