# Let a tuple (x, y) represent a point in a Cartesian system. Write a function that receives as a parameter a list of
# points and returns a list of unique tuples (a, b, c) representing the unique lines determined by those points ((a,
# b, c) corresponds to the right ax + by +c  = 0).

# Mentiune: nu exista doar o singura ecuatie...(ax + by + c = 0 si 5*ax + 5*by + 5*c = 0)


def line_ecuation(a):
    if len(a) < 2:
        return 'Error: list contains less than two points!The line ecuation cannot be determined with less than two points!'
    result = (0, 0, 0)
    x1 = a[0][0]
    y1 = a[0][1]
    x2 = a[1][0]
    y2 = a[1][1]
    if x1 == x2:
        result = ((y2 - y1), 0, -x1 * (y2 - y1))
    else:
        result = (-((y2 - y1) / (x2 - x1)), 1, (x1 * ((y2 - y1) / (x2 - x1)) - y1 * ((y2 - y1) / (x2 - x1))))
    for element in a[1:]:
        if result[0] * element[0] + result[1] * element[1] + result[2] != 0:
            return 'Error: the given points do not form a line!'
    return result


if __name__ == '__main__':
    print(line_ecuation([(-1, 0), (-3, -2)]))