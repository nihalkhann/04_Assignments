def main():

    fruit_list = ['apple', 'banana', 'watermelon', 'grapes', 'pineapple']

    print("Length of the list:", len(fruit_list))

    fruit_list.append('mango')

    print("Updated list:")
    for fruit in fruit_list:
        print(fruit)

if __name__ == '__main__':
    main()
