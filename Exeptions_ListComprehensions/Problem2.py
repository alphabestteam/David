if __name__ == "__main__":
    try:
        num1 = int(input("Enter first int: "))
        num2 = int(input("Enter second int: "))
    except ValueError:
        print("You didn't enter an int value")

    print("Finished running")
