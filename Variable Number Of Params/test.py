def my_fun(*args, **kwargs):
    print(args)
    print(kwargs)


numbers = [3, 4, 1, 3, 123, 3]
my_fun(3, 2, 123, 41231, 3, 123, word="wind", letter="d", number=3)
