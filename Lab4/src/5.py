# Să se scrie o funcție care primește ca argumente două șiruri de caractere, target și to_search șireturneaza o listă de fișiere care conțin to_search. Fișierele se vor căuta astfel: dacă target este un fișier, se caută doar in fișierul respectiv iar dacă este un director se va căuta recursiv in toate fișierele din acel director. Dacă target nu este nici fișier, nici director, se va arunca o excepție de tipul ValueError cu un mesaj corespunzator.
import os


def ex_5(target, to_search):
    try:
        if os.path.isfile(target):
            with open(target) as f:
                if to_search in f.read():
                    return True
            return False
        elif os.path.isdir(target):
            nr_of_files = 0
            result = False
            for (root, directories, files) in os.walk(target):
                for fileName in files:
                    full_fileName = os.path.join(root, fileName)
                    if ".txt" in fileName:
                        nr_of_files += 1
                        with open(full_fileName, 'r') as f:
                            if to_search in f.read():
                                return True
            if not nr_of_files:
                raise ValueError
            return result
        else:
            raise Exception("The given path is not a file and is not a direcoty!")
    except ValueError:
        return "No files were found in the directory from the given path!"
    except Exception as error:
        return error


if __name__ == '__main__':
    print(ex_5("/home/s/Downloads", "."))
