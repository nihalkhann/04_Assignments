MAX_TERM_VALUE : int = 10000

def main():
    a = 0 
    b = 1 
    while a <= MAX_TERM_VALUE:
        print(a)
        c = a + b
        a = b
        b = c


if __name__ == '__main__':
    main()