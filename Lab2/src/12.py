# Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple. Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]


# take second element for sort
import random


def take_last_of_second(elem):
    return elem[1][-1]


def ex_12(l):
    l.sort(key=take_last_of_second)
    return l


if __name__ == '__main__':
    print(ex_12([('abc', 'bcd'), ('abc', 'zza')]))
