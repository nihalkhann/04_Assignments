def main():
    a = int(input('Enter temperature in Fahrenheit: '))
    celsius = (a - 32) * 5.0/9.0
    print(f'Temperature {a}°F = {celsius:.3f}°C')
if __name__ == '__main__':
    main()