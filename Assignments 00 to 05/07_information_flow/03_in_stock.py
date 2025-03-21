def main():
	fruit : str = input("Enter a fruit: ")
	stock = num_in_stock(fruit)
	if stock == 0:
		print("This fruit is not in stock.")
	else:
		print(f"This fruit is in stock! Here is how many: \b{stock}")
		


def num_in_stock(fruit):
	
	if fruit == 'mango':
		return 500
	if fruit == 'apple':
		return 150
	if fruit == 'banana':
		return 120
	else:
		print(f"{fruit} is not in Stock")
		return 0


if __name__ == '__main__':
    main() 