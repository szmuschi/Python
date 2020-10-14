# Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start position (integer). The function will return the song composed by going though the musical notes beginning with the start position and following the moves given as parameter.
# 	Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]

def song(notes, numbers, start):
    n = len(notes)
    ind = start
    result = []
    result.append(notes[ind % n])
    for el in numbers:
        ind = ind + el
        result.append(notes[ind % n])
    return result


if __name__ == '__main__':
    print(song(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))