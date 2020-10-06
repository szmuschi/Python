# Write a function that validates if a number is a palindrome.

def is_palindrome():
    print('Function that validates if a number is a palindrome')
    nr = int(input("Enter number: "))
    nr_copy = nr
    rev_nr = 0
    while nr > 0:
        rev_nr = rev_nr * 10 + nr % 10
        nr = nr // 10
    else:
        if rev_nr == nr_copy:
            print('The introduced number is a palindrome!')
            return True
        else:
            print('The introduced number is not a palindrome!')
            return False


if __name__ == '__main__':
    is_palindrome()
