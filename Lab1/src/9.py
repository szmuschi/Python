# Write a functions that determine the most common letter in a string. For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.

import re


def most_frequent():
    print('Function that determines the most common letter in a string')
    text = input('Enter string: ')
    text = re.sub('[^a-zA-Z]', '', text)
    frequencies = [(c, text.count(c)) for c in set(text)]
    max_nr = max(frequencies, key=lambda x: x[1])[1]
    result = [s for s in frequencies if s[1] == max_nr]
    print('The result is: ', result)
    return result


if __name__ == '__main__':
    most_frequent()