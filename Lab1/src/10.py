# Write a function that counts how many words exists in a text. A text is considered to be form out of words that are separated by only ONE space. For example: "I have Python exam" has 4 words.

def nr_of_words():
    print('Function that counts how many words exists in a text')
    string = input("Enter text: ")
    if len(string) == 0:
        print('The introduced string does not contain any words!')
        return 0
    result = string.count(' ')
    if string[0] != ' ':
        result = result + 1
    print('The string that was introduced contains ', result, ' words')
    return result


if __name__ == '__main__':
    nr_of_words()
