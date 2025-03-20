def main():
    lst = []

    a = input("Enter a value ")
    while a :
        lst.append(a)
        a = input("Enter a  value")

        print(f"Here's is the list:  {lst}")


if __name__ == '__main__':
    main()