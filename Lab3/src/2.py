# Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters in the character string and the values are the number of occurrences of that character in the given text.
# Example: For string "Ana has apples." given as a parameter the function will return the dictionary: {'A': 1, '': 2, 'n': 1, 'a': 2, 'r': 2, '.': 1}.

def ex_2(s):
    result = {}
    for letter in s:
        n = result.get(letter, 0)
        result[letter] = n + 1
    return result
    # return {letter: s.count(letter) for letter in set(s)}
    # result = {}
    # for letter in set(s):
    #     result.update({letter: s.count(letter)})
    # return result


if __name__ == '__main__':
    print(ex_2("Ana has apples."))
