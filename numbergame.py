from random import randint


def secret_number(a, b):
    """
    Chooses a random integer s between a and b. s is the zjmm.
    """
    s = randint(a,b)
    return s

def print_response(x, s, a, b):
    if x < a or x > b:
        print 'Please enter a number between %d and %d' % (a, b)
        return a, b
    if x > s:
        print 'The number is between %d and %d' % (a, x)
        return a, x
    else:
        print 'The number is between %d and %d' % (x, b)
        return x, b

def run_zjmm(a, b):
    s = secret_number(a, b)
    guess = int(raw_input('Make a guess: '))
    while guess != s:
        a, b = print_response(guess, s, a, b)
        guess = int(raw_input('Make a guess: '))
    else:
        print 'ZJMM!'


a = int(raw_input('Enter the smallest number:'))
b = int(raw_input('Enter the largest number:'))

run_zjmm(a, b)
