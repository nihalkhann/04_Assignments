def main():
    dividend : int = int(input('Please enter an Number to be divided: '))
    divisor : int = int(input('Please enter the Number to divided by: '))

    quotient: int = dividend // divisor
    remainder: int = dividend % divisor

    print(f"The result of this division is {quotient} with a  remiander of {remainder}.")
if __name__ == '__main__':
    main()