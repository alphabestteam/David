import time


def timer(func):
    def in_func(*args, **kwargs):
        start_time = time.time()
        x = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time it took: {end_time - start_time} seconds")
        return x

    return in_func


@timer
def calc_sum(numbers: list) -> int:
    total = sum(numbers)
    return total


if __name__ == '__main__':
    number_list = [*range(1, 1000000)]
    print(calc_sum(number_list))
