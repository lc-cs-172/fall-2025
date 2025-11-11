
##----------------------------------------------------------------

import time

time_is_now = time.asctime()

print("""
    ==== The time is now ====
""", time_is_now, """
    ==== The time is now ====
""");

time_starting = None
time_finished = None

references_used = None

##----------------------------------------------------------------

def problem_1_gather_special(is_special, limit):
    """Problem 1:

    Returns a list of all positive integers less than or equal to limit
    for which is_special(n) is True.

    Must use an expression with list comprehension, including the
    conditional *if* phrase, to create the list.

    """
    pass

##----------------------------------------------------------------

def problem_2_find_minimum(p, lo, hi, tol=1e-7):
    """Problem 2:

    Given a quadratic polynomial p, assume there is a single local
    minimum (x,p(x)) with lo < x and x < hi.  

    tol is the tolerance; any value v such that abs(v) < tol is
    considered close enough to 0.

    Note that p is a quadratic function -- the graph is a parabola --
    it's smooth and convex.  

    In this case, we know that if we have 3 values x0 < x1 < x2 where
    p(x0) > p(x1) and p(x1) < p(x2), the minimum must lie between x0 and
    x2.  We know x1 is close enough to the minimum if x0 is close enough
    to x2.

    Using recursion with bisection, find the interval holding the
    minimum, and return (x0,x2)

    """
    return (0,0)

##----------------------------------------------------------------

"""Problem 3:

    Implement the set of routines below to dynamically maintain the
    current average of all the values x[i] added since initializaton,
    using O(1) global storage and O(1) time for each operation.

    Recall that the average of a list of numbers x[i] is sum(x)/len(x).

    Note: you are not allowed to store all the x[i].  

    Yes, that's right, O(1) storage -- you may not store every value
    added -- you can only use a constant amount of storage.

    Find and implement a way to incrementally maintain the current
    average.

"""

def problem_3_fast_avg_init():
    """initialze problem_3_fast_avg working values"""
    pass

def problem_3_fast_avg_add(x):
    """add the next value to the average"""
    pass

def problem_3_fast_avg_get():
    """return the overall average"""
    pass

##----------------------------------------------------------------

"""Problem 4:

    Purpose: demonstrate that constants matter, where we prove by
    example that sometimes f(x) in O(n lg n) can be greater than g(x) in
    O(n^2) for hundreds of values.

    For this problem, only consider integers n > 0.  N is a constant,
    set to PROBLEM_4_BREAKPOINT.  Find other constants (scale,offset)
    such that f(n) > g(n) for all n < N, and f(n) < g(n) for all n > N.
    Note that comparing f(N) with g(N) is not specified.

    Implement problem_4_f() and problem_4_get_constants().
    Leave problem_4_g() alone.
"""

## NB: This is a FIXED constant -- we will not change it
PROBLEM_4_BREAKPOINT = 128

def problem_4_f(x, scale, offset):
    """return  scale * (x * lg  x) + offset"""
    pass

def problem_4_get_constants():
    """return (scale,offset) such that 
    problem_4_f(x,scale,offset) > problem_4_g(x)     1 <= x < PROBLEM_4_BREAKPOINT
    problem_4_f(x,scale,offset) < problem_4_g(x)              PROBLEM_4_BREAKPOINT <  x

    I expect you to find those values "offline", and just plug in
    constants that work, given that the crossover point is fixed.
    """
    return (0,0)

def problem_4_g(x):
    """defines our fixed O(n^2) function needed in the crossover calculation"""
    return (x*x)/4;

##----------------------------------------------------------------

##[]##
