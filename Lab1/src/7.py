# Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will return 123, or if the text is "abc123abc" the function will extract 123). The function will extract only the first number that is found.

import re


def extract_number():
    print('Function that extract first number from a text')
    string = input("Enter string: ")
    if re.search('[0-9]', string):
        result = re.search(r'[0-9][0-9]*', string)[0]
        print('The result is ', result)
        return result
    else:
        print('The introduced string does not contain numbers!')
        return ''


if __name__ == '__main__':
    extract_number()
