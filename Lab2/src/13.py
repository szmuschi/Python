# Write a function that will receive a list of words  as parameter and will return a list of lists of words, grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.
#
# Example:
#
# group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]


def take_last_two(elem):
    return elem[-2]


def ex_13(l):
    l.sort(key=take_last_two)
    result = []
    last_rhyme = l[0][-2:]
    var = []
    for el in l:
        if el[-2:] == last_rhyme:
            var.append(el)
        else:
            result.append(var)
            var = [el]
            last_rhyme = el[-2:]
    if var:
        result.append(var)
    return result


if __name__ == '__main__':
    print(ex_13(['ana', 'banana', 'carte', 'arme', 'parte']))