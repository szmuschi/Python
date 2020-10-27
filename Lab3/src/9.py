# Write a function that receives a variable number of positional arguments and a variable number of keyword arguments adn will return the number of positional arguments whose values can be found among keyword arguments values.
# #
# # Ex: my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5) will return returna 3


def ex_9(*args, **kwargs):
    return [el for el in args if el in kwargs.values()]
    result = 0
    for element in args:
        if element in kwargs.values():
            result = result + 1
    return result


if __name__ == '__main__':
    print(ex_9(1, 2, 3, 4, x=1, y=2, z=3, w=5))
