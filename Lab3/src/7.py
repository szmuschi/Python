# Write a function that receives a variable number of sets and returns a dictionary with the following operations from all sets two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b", where a and b are two sets, and op is the applied operator: |, &, -.
#
# Ex: {1,2}, {2, 3} =>
#
# {
#
#     "{1, 2} | {2, 3}": 3,
#
#     "{1, 2} & {2, 3}": 1,
#
#     "{1, 2} - {2, 3}": 1,
#
#     ...
#
# }


def ex_7(*args: set):
    result = {}
    op = {"|": lambda a, b: a | b,
          "&": lambda a, b: a & b,
          "-": lambda a, b: a - b}
    for i in range(len(args) - 1):
        for j in range(i + 1, len(args)):
            for o in op.keys():
                my_key = f"{args[i]} {o} {args[j]}"
                my_value = op[o](args[i], args[j])
                result[my_key] = my_value
                if o == "-":
                    my_key = f"{args[j]} {o} {args[i]}"
                    my_value = op[o](args[j], args[i])
                    result[my_key] = my_value
            # intersection = args[i].intersection(args[j])
            # union = args[i].union(args[j])
            # a_b = args[i].difference(args[j])
            # b_a = args[j].difference(args[i])
            # my_key = f"{args[i]} & {args[j]}"
            # result[my_key] = intersection
            # my_key = f"{args[i]} | {args[j]}"
            # result[my_key] = union
            # my_key = f"{args[i]} - {args[j]}"
            # result[my_key] = a_b
            # my_key = f"{args[j]} - {args[i]}"
            # result[my_key] = b_a
    return result


if __name__ == '__main__':
    print(ex_7({1, 2}, {2, 3}, {4, 5}))
