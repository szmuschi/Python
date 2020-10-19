# Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True. For each string, generate a list containing the characters that have the ASCII divisible by x if the flag is set to True, otherwise it should contain characters that have the non-xvid ASCII code.
# Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" . Note: The function must return list of lists.

def ex_9(str_list, number=1, flag=True):
    result = []
    for string in str_list:
        for element in string:
            if flag and ord(element) % number == 0:
                result.append(element)
            elif not flag and ord(element) % number:
                result.append(element)
    result = [el for el in set(result)]
    return result


if __name__ == '__main__':
    print(ex_9(["test", "hello", "lab002"], 2, False))
