def add_five_copies(my_List, data):

       for i in range(5):
        my_List.append(data)

def main():
    message = input("Enter your message to copy: ")
    my_list = []
    print(f"List before {my_list}")
    add_five_copies(my_list, message)
    print(f"List after {my_list}")

if __name__ == "__main__":
    main()