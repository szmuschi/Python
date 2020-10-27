# Să se scrie o funcție ce primeste un singur parametru, director, ce reprezintă calea către un director.
#
# Funcția returnează o listă cu extensiile unice sortate crescator (in ordine alfabetica) a fișierelor din directorul
# dat ca parametru.
#
# Mențiune: extensia fișierului ‘fisier.txt’ este ‘txt’
import os


def ex_1(directory_path):
    try:
        result = []
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        for file in files:
            ext = os.path.splitext(file)[1][1:]
            if ext not in result and len(ext):
                result.append(ext)
        result.sort()
        return result
    except Exception as error:
        return error


if __name__ == '__main__':
    print(ex_1("/home/s/Downloads"))
