def main():

    fruits = {
        'apple': 6,
        'banana': 5,
        'orange': 3,
        'grape': 4
    }

    total  = 0

    for name in fruits:
        price = fruits[name]
        amount = int(input(f"How many {name} do you want to buy? "))
        total += (price * amount)

        print(f"You bought {amount} {name}s, and the total cost is {total}." )

if __name__ == '__main__':
    main()