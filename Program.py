def sum_nums_in_list(number_list):
    return sum(number_list)


def calc_pow(num):
    return num*num


def check_num_primary(number):
    for temp_num in range(2, number):
        if number % temp_num == 0:
            return f"\n{number} is NOT primary"
    return f"\n{number} is primary"


if __name__ == '__main__':
    numbers = range(1, 100)
    print(sum_nums_in_list(numbers))
    print(calc_pow(5), calc_pow(6), calc_pow(7), calc_pow(8))
    print(check_num_primary(5), check_num_primary(6), check_num_primary(7), check_num_primary(14), check_num_primary(152), check_num_primary(60693))
