# Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)
import numpy as np


def list_operations(a, b):
    a = np.array(a)
    b = np.array(b)
    reunion = np.union1d(a, b)
    intersection = np.intersect1d(a, b)
    a_b = np.array([])
    for el in a:
        if el not in b:
            a_b = np.union1d(a_b, [el])
    b_a = np.array([])
    for el in b:
        if el not in a:
            b_a = np.union1d(b_a, [el])
    result = {'reunion': reunion, 'intersection': intersection, 'a-b': a_b, 'b-a': b_a}
    return result


if __name__ == '__main__':
    print(list_operations([1, 3, 5, 7], [1, 2, 4, 8, 7]))