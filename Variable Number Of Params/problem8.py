def total_age(**ages: int) -> None:
    age_sum = 0
    for age_name, age_value in ages.items():
        print(f"name: {age_name}, age: {age_value}")
        age_sum += age_value
    print(f"\nAge sum: {age_sum}")


if __name__ == '__main__':
    total_age(ag1=10, age2=20, age3=30, age4=40)
