if __name__ == '__main__':
    array_size = 0
    input_incorrect = True
    while input_incorrect:
        try:
            array_size = int(input("Enter array size: "))
            input_incorrect = False
        except ValueError:
            print("Incorrect value please enter only ints")

    print([num ** 2 for num in range(1, array_size + 1)])
