import time
def main():
    for i in range(10, 0, -1):  
     print(f"{i}")
     time.sleep(1)  # ! artificial delay 
    print("Liftoff!")

if __name__ == '__main__':
    main()