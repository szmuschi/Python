# Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple contains the first items in the lists, the second element contains the items on the position 2 in the lists, etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1.5, "a ") ,(5, 6, "b"), (3,7, "c")].
# Note: If input lists do not have the same number of items, missing items will be replaced with None to be able to generate max ([len(x) for x in input_lists]) tuples.


def ex_11(*args):
    if args:
        result = []
        n = len(args)
        max_length = len(args[0])
        for l in args[1:]:
            if len(l) > max_length:
                max_length = len(l)
        for ind in range(max_length):
            s = ()
            for l in args:
                if ind < len(l):
                    s = s + (l[ind], )
                else:
                    s = s + (None, )
            result.append(s)
        return result


if __name__ == '__main__':
    print(ex_11([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))
