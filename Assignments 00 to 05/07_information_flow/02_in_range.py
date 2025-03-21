def in_range(n, low, high):
    
    return low <= n <= high

def main():
    
    n = int(input("Enter the number: "))
    low = int(input("Enter the lower limit: "))
    high = int(input("Enter the upper limit: "))
    
    if in_range(n, low, high):
        print(f"{n} is in the range [{low}, {high}].")
    else:
        print(f"{n} is not in the range [{low}, {high}].")

if __name__ == "__main__":
    main()
