# Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of unique elements in the list, and b representing the number of duplicate elements in the list (use sets to achieve this objective)


def ex_6(l):
    return (len([el for el in l if l.count(el) == 1]), len([el for el in l if l.count(el) != 1]))


if __name__ == '__main__':
    print(ex_6([1, 3, 1, 4, 2, 5]))
