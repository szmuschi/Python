# Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order (as in the example):
# firs      1  2  3  4    =>   first_python_lab
# n_lt      12 13 14 5
# oba_      11 16 15 6
# htyp      10 9  8  7


def spiral_print(a):
    n = len(a) - 1
    result = ''
    ind = 0
    while ind <= n/2:
        x = ind
        while x < n - ind + 1:
            result = result + a[ind][x]
            x = x + 1
        x = ind + 1
        while x < n - ind + 1:
            result = result + a[x][n - ind]
            x = x + 1
        x = n - ind - 1
        while x >= ind:
            result = result + a[n-ind][x]
            x = x - 1
        x = n - ind - 1
        while x >= ind + 1:
            result = result + a[x][ind]
            x = x - 1
        ind = ind + 1
    print(result)
    return result


if __name__ == '__main__':
    a = [['f', 'i', 'r', 's'],
         ['n', '_', 'l', 't'],
         ['o', 'b', 'a', '_'],
         ['h', 't', 'y', 'p']]
    spiral_print(a)
