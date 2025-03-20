country_a_age : int = 16
country_b_age : int = 25
country_c_age : int = 48

def main():
    user_age:int = int(input('How old are you? '))

    if user_age >= country_a_age:
        print(f'You can vote in Country A where the voting age is {country_a_age}')
    else:
        print(f'You cannot vote in Country A. You must be {country_a_age - user_age} years older')

    if user_age >= country_b_age:
        print(f'You can vote in Country B where the voting age is {country_b_age}')
    else:
        print(f'You cannot vote in Country B. You must be {country_b_age - user_age} years older')
    
    if user_age >= country_c_age:
        print(f'You can vote in Country C where the voting age is {country_c_age}')
    else:
        print(f'You cannot vote in Country C. You must be {country_c_age - user_age} years older')


if __name__ == '__main__':
    main()