def double(num: int):
    return num * 2


def main():
    a = int(input("Enter a number: "))
    b = double(a)
    print("Double that is", b)

if __name__ == '__main__':
    main()