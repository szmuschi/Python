# Write a function to return a list of the first n numbers in the Fibonacci string.


def fibonacci(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fibonacci_list = fibonacci(n - 1)
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
        return fibonacci_list


if __name__ == '__main__':
    print(fibonacci(1000))
