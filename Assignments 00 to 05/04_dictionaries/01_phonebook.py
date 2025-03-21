def read_phone_numbers():

    phone_book ={}

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number:  ")
        phone_book[name] = number

    return phone_book


def print_phone_numbers(phone_book):

    for name in phone_book:
        print(f"{name}: {phone_book[name]}")

def search_phone_numbers(phone_book):
    while True:
        name = input("Enter name to search:  ")
        if name == "":
            break
        if name not in phone_book:
            print(f"{name} not found.")
        else:
            print(phone_book[name])


def main():
    phone_book = read_phone_numbers()
    print_phone_numbers(phone_book)
    search_phone_numbers(phone_book)


if __name__ == "__main__":
    main()