def get_sum(*numbers):  # Packing
    return sum(numbers)


def unpack(arg1, arg2, arg3, arg4, arg5):  # Unpacking
    print(arg1, arg2, arg3, arg4, arg5)


if __name__ == '__main__':
    print(get_sum(3, 4, 21, 41, 2, 5))

    args_list = [1, 2, 3, 4, 5]
    unpack(*args_list)
