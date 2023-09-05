def sum_nums_in_list(number_list):
    return sum(number_list)


def calc_pow(num):
    return num*num


if __name__ == '__main__':
    numbers = range(1, 100)
    print(sum_nums_in_list(numbers))
    print(calc_pow(5), calc_pow(6), calc_pow(7), calc_pow(8))
