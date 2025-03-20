def add_many_numbers(numbers: list[int]) -> int:
    return sum(numbers)

def main():
    numbers = [0, 1, 2, 3, 4, 5]
    print(f"The sum of the numbers in the list is: {add_many_numbers(numbers)}")

if __name__ == '__main__':
    main()
