import time

def fibonacci(n):
    """return the nth Fibonacci Number"""
    assert n >= 0
    if 0 == n: return 0;
    if 1 == n: return 1;
    return fibonacci(n-2) + fibonacci(n-1)

def show_fibonacci(size = 10):
    print(f'==== fibonacci({size}) ====')
    starting = time.time()    
    sweep = [ fibonacci(n) for n in range(0,size) ]
    finished = time.time()
    duration = finished - starting
    print(sweep)
    print(f'==== used {duration:0.2e} seconds\n');

def demo_fibonacci(size=20):
    for i in range(0, size, 2):
        show_fibonacci(i)

#[]#
