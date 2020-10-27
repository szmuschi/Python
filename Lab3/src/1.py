# Write a function that receives as parameters two lists a and b and returns a set of sets containing: (a intersected with b, a reunited with b, a - b, b - a)


def list_operations(a, b):
    a = set(a)
    b = set(b)
    result = set([])
    result.add(frozenset(a.intersection(b)))
    result.add(frozenset(a.union(b)))
    result.add(frozenset(a.difference(b)))
    result.add(frozenset(b.difference(a)))
    return result


if __name__ == '__main__':
    print(list_operations([1, 2, 3, 5, 9], [1, 2, 4, 8, 7]))