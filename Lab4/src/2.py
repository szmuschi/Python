# Să se scrie o funcție ce primește ca argumente două căi: director si fișier.
#
# Implementati functia astfel încât în fișierul de la calea fișier să fie scrisă pe câte o linie, calea absolută a
# fiecărui fișier din interiorul directorului de la calea folder, ce incepe cu litera A.
import os


def ex_2(directory_path, file_path):
    try:
        result = []
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        for file in files:
            if file[0] == 'A':
                result.append(file)
        result.sort()
        with open(file_path, 'a') as the_file:
            for file_name in result:
                the_file.write(file_name)
        return result
    except Exception as error:
        return error



if __name__ == '__main__':
    print(ex_2("/home/s/Downloads", "../files/ex_2.txt"))
