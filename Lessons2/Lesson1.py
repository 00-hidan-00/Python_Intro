import logging
import uuid
from dataclasses import dataclass, field
from typing import TypeAlias, ClassVar

from pydantic import BaseModel, Field

T_NAME: TypeAlias = str


# class Human:
#     CLASS_ART: int = 42
#
#     def __init__(self, name: str, age: int = 18, pk: uuid.UUID = None):
#         self.name = name
#         self.age = age
#         self.pk = pk or uuid.uuid4()
#
#     @classmethod
#     def from_file(cls, path: pathlib.Path):
#         ...


@dataclass
class Human2:
    name: str
    age: int = field(default=18)
    pk: uuid.UUID = field(default_factory=uuid.uuid4)

    CLASS_ART: ClassVar = 42


class Human3(BaseModel):
    name: str = Field()
    age: int = Field(default=18)
    pk: uuid.UUID = Field(default_factory=uuid.uuid4)

    CLASS_ART: ClassVar = 42



def print_hi(name: str):
    print(f"Hi {name}")

    logging.warning("Hi there")


    human = Human3(name="Bob", age=20)
    # human_as_dict = human.__dict__
    serialize = human.json()
    new_human = Human3.parse_raw(serialize)

    print(new_human)

if __name__ == "__main__":
    print_hi('PyCharm')
