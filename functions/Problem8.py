from random import randint
from random import uniform


def random_int(start: int, end: int) -> int:
    return randint(start, end)


def random_double(start: float, end: float) -> float:
    return uniform(start, end)


if __name__ == '__main__':
    print(random_int(3, 5))
    print(random_double(3, 5))
