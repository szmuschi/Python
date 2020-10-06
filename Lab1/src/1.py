# Find The greatest common divisor of multiple numbers read from the console.

from math import gcd


def greatest_common_divisor():
    print('Function that calculates greatest common divisor.Introduce numbers:')
    n1 = int(input('Enter first number: '))
    n2 = int(input('Enter second number: '))
    n3 = (input('Enter number or quit(to quit): '))
    divisor = gcd(n1, n2)
    while n3 != 'quit':
        divisor = gcd(divisor, int(n3))
        n3 = (input('Enter number or quit(to quit): '))
    else:
        print('Greatest common divisor of all introduced numbers is ', divisor)
    return divisor


if __name__ == '__main__':
    greatest_common_divisor()
