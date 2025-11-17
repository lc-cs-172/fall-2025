




print("""
Purpose: demo list comprehension and other Python nits and bits
""")

##----------------------------------------------------------------
##----------------------------------------------------------------

## Resource: Google AI:
## Q/ how do I check if an integer is prime in Python?
## A/ below

import math

def is_prime(n):
    # Prime numbers are positive integers greater than 1
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # All other even numbers are not prime
    if n % 2 == 0:
        return False
    
    # Check for divisibility by odd numbers from 3 up to the square root of n
    # We only need to check up to int(math.sqrt(n)) because if a number n has a factor greater than its square root, 
    # it must also have a corresponding factor smaller than its square root.
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
        if n % i == 0:
            return False
            
    return True

# Example Usage:
number1 = 17
if is_prime(number1):
    print(f"{number1} is a prime number.")
else:
    print(f"{number1} is not a prime number.")

number2 = 30
if is_prime(number2):
    print(f"{number2} is a prime number.")
else:
    print(f"{number2} is not a prime number.")

##----------------------------------------------------------------
##----------------------------------------------------------------

is_special = lambda x: \
    ((type(x) is int and is_prime(x))
    or
    (type(x) is tuple and is_prime(x[0])))


def demo_list_comprehension():

    limit = 17
    zed_one = [0,1]

    int_solo = [ (i) for i in range(1,limit+1) if is_special(i) ]
    print('int_solo\n', int_solo);

    tuple_solo = [ (i,) for i in range(1,limit+1) if is_special(i) ]
    print('tuple_solo\n', tuple_solo);

    tuple_pair = [ (i,j)
                   for i in range(1,limit+1)
                   for j in zed_one
                   if is_special(i)
                  ]
    print('tuple_pair\n', tuple_pair);

demo_list_comprehension();

[]
