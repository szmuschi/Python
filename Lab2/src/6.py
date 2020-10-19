# Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).
def matrix_transformation(a):
    res = list(a[:])
    n = len(res)
    for i in range(n):
        for j in range(n):
            if i + j >= n:
                res[i][j] = 0
    return res


if __name__ == '__main__':
    a = [[0, 1, 2, 3, 4],
         [3, 4, 5, 6, 7],
         [6, 7, 8, 8, 9],
         [3, 4, 5, 1, 6],
         [5, 2, 7, 78, 1]]
    print(matrix_transformation(a))
