# Să se scrie o funcție care primește ca parametru un șir de caractere care reprezintă calea către un fișer si returnează un dicționar cu următoarele cămpuri: full_path = calea absoluta catre fisier, file_size = dimensiunea fisierului in octeti, file_extension = extensia fisierului (daca are) sau "", can_read, can_write = True/False daca se poate citi din/scrie in fisier.
import os


def ex_7(file_path):
    return {'full_path': os.path.abspath(file_path),
            'file_size': os.path.getsize(file_path),
            'file_extension': os.path.splitext(file_path)[1][1:],
            'can_read': os.access(file_path, os.R_OK),
            'can_write': os.access(file_path, os.W_OK)}

# gresit
def test(path):
    for file in os.listdir(path):
        var = os.path.abspath(file)
        print(var)


if __name__ == '__main__':
    print(ex_7("/home/s/Downloads/pip-labs-main.zip"))
    # print(test("/home/s/Downloads"))
    #
    # print(ex_7("../src/1.py"))
