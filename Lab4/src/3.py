# Să se scrie o funcție ce primește ca parametru un string my_path.
#
# Dacă parametrul reprezintă calea către un fișier, se vor returna ultimele 20 de caractere din conținutul
# fișierului. Dacă parametrul reprezintă calea către un director, se va returna o listă de tuple (extensie, count),
# sortată descrescător după count, unde extensie reprezintă extensie de fișier, iar count - numărul de fișiere cu
# acea extensie. Lista se obține din toate fișierele (recursiv) din directorul dat ca parametru.
import os


def ex_3(my_path):
    try:
        if os.path.isdir(my_path):
            result = []
            for (root, directories, files) in os.walk(my_path):
                for fileName in files:
                    result.append(fileName)
            result = [os.path.splitext(file)[1][1:] for file in result if len(os.path.splitext(file)[1])]
            result = [(extension, result.count(extension)) for extension in set(result)]
            return result
        elif os.path.isfile(my_path):
            textfile = open(my_path)
            textfile.seek(0, 2)
            textfile.seek(textfile.tell() - 20)
            result = textfile.read()
            # lines = textfile.readlines()
            # result = []
            # for line in reversed(lines):
            #     if len(result) < 20:
            #         result = line + result
            #     else:
            #         break
            # result = result[-20:]
            return result
    except Exception as error:
        return error


if __name__ == '__main__':
    print(len(ex_3("/home/s/Downloads/Resume.txt")))
