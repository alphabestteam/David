import math


def quadratic_equation(a: float, b: float, c: float) -> str or float:
    if a == 0:
        return "A cant be 0"
    calc_for_sqrt = (b ** 2 - 4 * a * c)
    if calc_for_sqrt < 0:
        return "Cant do sqrt on negative numbers"
    x1 = -b + (math.sqrt(calc_for_sqrt) / (a * 2))
    x2 = -b - (math.sqrt(calc_for_sqrt) / (a * 2))
    return x1, x2


if __name__ == '__main__':
    print(quadratic_equation(3, 4, -3))
