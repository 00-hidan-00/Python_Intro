from typing import ClassVar

from Test_Project.app.typing import T_Subjects, T_Name


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

