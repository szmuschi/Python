# Write a function that receives a list of numbers and returns a list of the prime numbers found in it.


def is_number_prime(n):
    # prime numbers are greater than 1
    if n > 1:
        # check for factors
        for i in range(2, int(n ** 0.5) + 1):
            if (n % i) == 0:
                return False
        else:
            return True

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        return False


def prime_numers_in_list(a):
    a = list(dict.fromkeys(a))
    result = []
    for element in a:
        if is_number_prime(element):
            result.append(element)
    return result


if __name__ == '__main__':
    print(prime_numers_in_list([4, 3, 7, 11, 9, 21, 23, 29, 47, 50]))
