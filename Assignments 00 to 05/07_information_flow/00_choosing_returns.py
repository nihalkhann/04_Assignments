ADULT_AGE : int = 18 

def is_adult(age: int):
    if age >= ADULT_AGE:
        print("You are Adult")
        return True
    else:
        print("You are not Adult")
    
    return False
    

def main():
    age : str = int(input("How old is this person?: "))
    print(is_adult(age))
    

if __name__ == "__main__":
    main()