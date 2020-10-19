# Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements. The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be the greatest palindrome number.


def is_palindrome(nr):
    nr_copy = nr
    rev_nr = 0
    while nr > 0:
        rev_nr = rev_nr * 10 + nr % 10
        nr = nr // 10
    else:
        if rev_nr == nr_copy:
            return True
        else:
            return False


def function(a):
    nr = 0
    palindrome = False
    for el in a:
        if is_palindrome(el):
            nr = nr + 1
            if el > palindrome:
                palindrome = el
    return (nr, palindrome)


if __name__ == '__main__':
    print(function([12321, 23432, 3, 5, 1, 1234321, 61]))
