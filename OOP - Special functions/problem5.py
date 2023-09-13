class Point:
    def __init__(self, x: int, y: int) -> None:
        self._x = x
        self._y = y

    def __str__(self) -> str:
        return f"x value: {self._x}, y value: {self._y}"

    def __eq__(self, other: any) -> any:
        return self._y == other._y and self._x == other._y

    def __add__(self, other: any) -> any:
        return self._y + other._y, self._x + other._x


if __name__ == '__main__':
    p1 = Point(1, 2)
    p2 = Point(3, 4)

    print(p1 == p2)
    print(p1)
    print(p2)
    print(p1 + p2)

'''
    The reason we got False when we tried to check if they equal is because they arent the same object and dont have the
    same address.
    
    When we printed the objects we got the address of the object. Since we didnt overload the __str__ method, it went
    to the default __str__ method and printed the address of the objects.
'''
