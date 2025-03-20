Max_length:int = 3 
def shorten (lst):
    if len(lst) > Max_length:
        remove_random_number = lst.pop()
        return shorten(lst)

def get_lst():
    
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "": 
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)
    print("The list you entered is: ", lst)
    


if __name__ == '__main__':
    main()