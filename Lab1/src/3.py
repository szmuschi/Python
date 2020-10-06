# Write a script that receives two strings and prints the number of occurrences of the first string in the second.


def strstr():
    print('Function that receives two strings and counts the number of occurrences of the first string in the second')
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    count = str2.count(str1)
    print('First string,"', str1, '", appears ', count, ' times in the second string,"', str2, '"')
    return count


if __name__ == '__main__':
    strstr()
