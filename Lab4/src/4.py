# Să se scrie o funcție cu numele ce returnează o listă cu extensiile unice a fișierelor din directorul dat ca
# argument la linia de comandă (nerecursiv). Lista trebuie să fie sortată crescător.
#
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’, iar ‘fisier’ nu are extensie, deci nu va apărea în lista
# finală.
import os
import sys


def ex_4(path):
    try:
        # path = input('Introduce directory path: ')
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        result = []
        for file in files:
            ext = os.path.splitext(file)[1][1:]
            if ext not in result and len(ext):
                result.append(ext)
        result.sort()
        return result
    except Exception as error:
        return error


if __name__ == '__main__':
    # print(sys.argv)
    print(ex_4(sys.argv[1]))
