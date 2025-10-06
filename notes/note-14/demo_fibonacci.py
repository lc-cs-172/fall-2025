import time

memo_fib = {}
is_memoize = True
is_memoize = False


def fibonacci(n):
    """return the nth Fibonacci Number"""

    assert n >= 0

    if 0 == n: return 0;
    if 1 == n: return 1;

    if n in memo_fib: return memo_fib[n];

    result = fibonacci(n-2) + fibonacci(n-1)
    if is_memoize: memo_fib[n] = result

    return result


def show_fibonacci(size = 10):
    """ time and display the fibonacci sequence of size 'size' """

    print(f'==== fibonacci({size}) ====')

    starting = time.time()    
    sweep = [ fibonacci(n) for n in range(0,size) ]
    finished = time.time()
    duration = finished - starting

    print(sweep)
    print(f'==== used {duration:0.2e} seconds\n');


def demo_fibonacci(size=36):
    for i in range(0, size+1, 2):
        show_fibonacci(i)


demo_fibonacci(12)

#[]#
