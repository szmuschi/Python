# Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"


def number_of_1_bits():
    print('Function that counts how many bits with value 1 a number has')
    nr = int(input("Enter number: "))
    bin_string = bin(nr)
    counter = bin_string.count('1')
    print('The introduced number has the binary form ', bin_string[2:], ' and contains ', counter, ' bits of "1"')
    return counter


if __name__ == '__main__':
    number_of_1_bits()
