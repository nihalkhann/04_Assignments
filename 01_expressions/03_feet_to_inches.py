
Inches_in_feet = 12 
def main():
    feet :float = float(input("Enter number of feet "))
    inches :float = feet * Inches_in_feet
    print(f"{feet} feet is equal to {inches} inches!")

if __name__ == '__main__':
    main()