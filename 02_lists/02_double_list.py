def main():
    numbers:list[int] = [1, 2, 3, 4]

    for i in range(len(numbers)):
        a = numbers[i]
        numbers[i] = a * 2 

    print(f"{numbers}")
if __name__ == '__main__':
    main()