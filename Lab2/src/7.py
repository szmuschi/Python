# Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list containing the items that appear exactly x times in the incoming lists.
# Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists [1,2,3] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.


def function(a, n):
    print(a)
    result = []
    b = set(a)
    for el in b:
        if a.count(el) == n:
            result.append(el)
    return result

# def f(*args):
#     print(args)
#     for arg in args:
#         print(arg)


def ex_7(x, *args):
    result = []
    all_lists = []
    for l in args:
        all_lists = all_lists + l
    all_lists = [i for i in l for l in args]
    result = function(all_lists, x)
    return result


if __name__ == '__main__':
    # print(ex_7(3, [12, 3, 24, 12, 12, 34, 3, 3]))
    print(ex_7(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
    # f(1, 3, [123, 57], "bg", (23, 12), { 'de': 344, 'fr': 98})
    # f()