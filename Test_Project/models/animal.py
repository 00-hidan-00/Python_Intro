from Test_Project.app.typing import T_Name




class Animal:
    def __init__(self, name: T_Name, age: int):
        self.name = name
        self.age = age

    def speak(self):
        return f'i\'m {self.name}. I\'m {self.age}'
