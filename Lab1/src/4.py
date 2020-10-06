# Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

import string


def lowercase_with_underscores():
    print('Function that converts a string of characters written in UpperCamelCase into lowercase_with_underscores')
    input_string = input("Enter string: ")
    input_string = input_string[0].lower() + input_string[1:]
    for c in string.ascii_uppercase:
        input_string = input_string.replace(c, '_' + c)
    input_string = input_string.lower()
    print('The transformed string is: ', input_string)
    return input_string


if __name__ == '__main__':
    lowercase_with_underscores()
