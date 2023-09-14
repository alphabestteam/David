def generator(n: int):
    num1 = 1
    num2 = 2
    while n >= 1:
        yield num1 * num2
        num1, num2 = num2, num1*num2
        n -= 1


if __name__ == '__main__':
    fibonacci = generator
    for number in fibonacci(10):
        print(number)
