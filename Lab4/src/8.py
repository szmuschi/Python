# Să se scrie o funcție ce primește un parametru cu numele dir_path. Acest parametru reprezintă calea către un director aflat pe disc. Funcția va returna o listă cu toate căile absolute ale fișierelor aflate în rădăcina directorului dir_path.
import os


def ex_8(directory_path):
    return [os.path.join(directory_path, f) for f in set(os.listdir(directory_path)) if os.path.isfile(os.path.join(directory_path, f))]



if __name__ == '__main__':
    print(ex_8("/home/s/Downloads/"))
