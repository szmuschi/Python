# Să se scrie o funcție care are același comportament ca funcția de la exercițiul anterior, cu diferența că primește un parametru în plus: o funcție callback, care primește un parametru, iar pentru fiecare eroare apărută în procesarea fișierelor, se va apela funcția respectivă cu instanța excepției ca parametru
import os


def callback_error(error):
    print(error)


def ex_6(target, to_search, callback):
    try:
        if os.path.isfile(target):
            with open(target) as f:
                if to_search in f.read():
                    return True
            return False
        elif os.path.isdir(target):
            nr_of_files = 0
            for (root, directories, files) in os.walk(target):
                for fileName in files:
                    full_fileName = os.path.join(root, fileName)
                    if ".txt" in fileName:
                        nr_of_files += 1
                        with open(full_fileName, 'r') as f:
                            if to_search in f.read():
                                return True
            if not nr_of_files:
                raise ValueError("No files were found in the directory from the given path!")
            return False
        else:
            raise Exception("The given path is not a file and is not a direcoty!")
    except Exception as error:
        callback(error)


if __name__ == '__main__':
    result = ex_6("/home/s/Download", ".", callback_error)
    # if result:
    #     print(result)
    # path = "/home/s/Downloads/pip-labs-main.zip"
    # print(os.path.isfile(path))
    # print(os.path.isdir(path))

