import random


def get_random_name_age_id() -> str and int:
    random_name = random.choice(["David", "Joe", "Jack",
                                 "Ben", "Chaim", "Ezra",
                                 "Paz", "Noam", "Dan", "Gorge"])
    random_id = random.choice(
        [94234, 23475, 12839, 12304, 76567,
         35234, 17454, 24452, 23457, 23423,
         97492, 12831, 95985, 87765, 39199])

    random_age = random.randint(1, 100)

    return random_name, random_id, random_age


class Person:
    def __init__(self) -> None:
        person_name, person_id, person_age = get_random_name_age_id()
        self._name = person_name
        self._id = person_id
        self._age = person_age

    def __str__(self) -> str:
        return f"Name: {self.name} Age: {self.age} ID: {self.id}"

    @property
    def name(self) -> str:
        return str(self._name)

    @property
    def age(self) -> int:
        return int(self._age)

    @property
    def id(self) -> int:
        return int(self._id)

    @name.setter
    def name(self, name) -> None:
        self._name = name

    @age.setter
    def age(self, age: int) -> None:
        self._age = age

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

