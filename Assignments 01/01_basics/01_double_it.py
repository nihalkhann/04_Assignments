def main():
    a = int(input('Enter a number to double it: '))
    b = 2  
    while a < 100:
        doubled_value = a * b
        print(f"{a} doubled is {doubled_value}")
        a = doubled_value  

if __name__ == '__main__':
    main()
