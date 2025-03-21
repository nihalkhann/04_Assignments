Minimum_height :int = 5;

def main():
    height:float = float(input("How tall are you in feets?: "))

    if height >= Minimum_height and height <=8:
        print("You're tall enough to ride!")
    elif height > 8:
        print("Don't lie, buddy!!!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()