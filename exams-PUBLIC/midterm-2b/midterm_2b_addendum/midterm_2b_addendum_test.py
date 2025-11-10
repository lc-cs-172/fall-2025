import os
import time
import math

is_select_answer = os.getenv('LC_CS_172_SELECT_ANSWER')

print(f'DEBUG: is_select_answer={is_select_answer}')

if is_select_answer:
    import _HIDDEN_midterm_2b_addendum as dut
else:
    import midterm_2b_addendum as dut

##----------------------------------------------------------------

def localtime_convert(line):
    format = '%a %b %d %H:%M:%S %Y'
    format = '%c'
    oo = time.strptime(line, format)
    oo = time.mktime(oo)
    return oo

def test_timed():
    print("""
==== test_timed underway ====
""")

    max_time_allowed = 3600

    time_starting = dut.time_starting
    time_finished = dut.time_finished

    assert time_starting
    assert time_finished

    clock_head = localtime_convert(time_starting)
    clock_tail = localtime_convert(time_finished)
    print(time_starting, '(starting) ->', clock_head)
    print(time_finished, '(finished) ->', clock_tail)

    assert clock_head < clock_tail

    clock_used = clock_tail - clock_head
    if 0 < clock_used and clock_used <= max_time_allowed:
        pass
    else:
        print("================================================================")
        print("Warning: total time taken %d exceeds maximum allowed %d" % (clock_used,max_time_allowed))
        print("================================================================")

    time_now = time.asctime()
    clock_now = localtime_convert(time_now)
    print(time_now, '(current)  ->', clock_now)

    ok_delay = 5*60
    assert clock_head < clock_now and (clock_now < clock_tail + ok_delay), (
        "pytest was run in valid window (time_starting, time_finished + %d seconds)") %(ok_delay)

def test_references():
    assert dut.references_used

##----------------------------------------------------------------

def double_factorial(n):
    '''return double factorial of n'''
    if 0 == n: return 1
    if 1 == n: return 1
    return n * double_factorial(n-2)

def test_problem_1():
    def is_special(n):
        y = double_factorial(n)
        return (y & 0x1)

    size = double_factorial(6);
    want = [ i for i in range(1,size+2,2) ]
    have = dut.problem_1_gather_special(is_special, size+1)
    assert have == want

##----------------------------------------------------------------

def test_problem_2():
    x_min = math.pi
    p = lambda x: scale*(x-x_min)**2 + 25
    lo = 0.0
    hi = 11.0
    ## NB: it is so flat at the bottom, we must scale up to succeed, and reduce tigher tolerances
    scales = [1e1, 1e2, 1e3]
    for tol in [10**(-d) for d in range(5,8) ]:
        for scale in scales:
            x0,x2 = dut.problem_2_find_minimum(p, lo, hi, tol)
            if 0: print('DEBUG:', 'scale:', scale, 'x0:', x0, 'x2:', x2)
            assert x0 < x2

            ## min has to be close enough
            width = x2 - x0
            assert 0 < width and width < tol

            ## min has to be within interval
            d0 = x_min - x0
            d2 = x2 - x_min
            assert (d0) < width
            assert (d2) < width
    
##----------------------------------------------------------------

def test_problem_3():

    items = []
    dut.problem_3_fast_avg_init()
    for item in ( i*2 - 41 for i in range(20) ):
        items.append(item)
        dut.problem_3_fast_avg_add(item)
        want = sum(items)/len(items)
        have = dut.problem_3_fast_avg_get()
        assert abs(have-want) < 1e-13
        
##----------------------------------------------------------------

def test_problem_4():

    ## make sure we got the right f
    ## XXX: something was way whacky when we went math.log(x)*math.log(2) instead of math.log2(x) ... 
    want_f = lambda x: scale*(x*math.log2(x)) + offset
    have_f = lambda x: dut.problem_4_f(x, scale, offset)
    for scale in (10**d for d in range(-3,3)):
        for offset in range(-200,201,20):
            for n in range (1,20):
                n = float(n)
                want_y = want_f(n)
                have_y = have_f(n)
                assert abs(want_y - have_y) < 1e-13

    scale,offset = dut.problem_4_get_constants()
    f = have_f
    g = dut.problem_4_g

    ## make sure we got the right relationships with f and g before and after the crossover N

    N = dut.PROBLEM_4_BREAKPOINT

    for n in range(1,N+1):
        n = float(n)
        if n < N: assert f(n) > g(n)
        assert f(n) < f(n+1)
        assert g(n) < g(n+1)

    for n in range(N+1,N*3):
        n = float(n)
        assert f(n) < g(n)
        assert f(n) < f(n+1)
        assert g(n) < g(n+1)

##[]##
