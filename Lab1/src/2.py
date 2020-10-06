# Write a script that calculates how many vowels are in a string.


def vowel_counter():
    print('Function that count number of vowels in the introduced string')
    string = input("Enter string: ")
    string = string.lower()
    count = string.count('a') + string.count('e') + string.count('i') + string.count('o') + string.count('u')
    print('The string that was introduced contains ', count, ' vowels')
    return count


if __name__ == '__main__':
    vowel_counter()
