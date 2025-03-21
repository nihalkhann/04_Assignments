def main():
    user = input("Please type a message: ")
    multiply = input(f"{user}! Enter a number of times to repeat your message:")

    for i in range(int(multiply)):
        print(user)


if __name__ == '__main__':
    main()