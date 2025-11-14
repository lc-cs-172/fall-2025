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

    max_time_expected = 3600

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
    if 0 < clock_used and clock_used <= max_time_expected:
        pass
    else:
        print("================================================================")
        print("Warning: total seconds taken %d exceeds maximum expected %d" % (clock_used,max_time_expected))
        print("================================================================")

    time_now = time.asctime()
    clock_now = localtime_convert(time_now)
    print(time_now, '(current)  ->', clock_now)
    assert clock_head < clock_now, "time_starting < time_current"

    max_delay_seconds = 15*60
    now_delay_seconds = clock_now - clock_tail
    assert now_delay_seconds < max_delay_seconds, (
        "pytest was run within %d seconds after time_finished)") %(max_delay_seconds)

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

    if 1:
        print("""
    =========================================
    ================ WARNING ================
       ==== Using quartic polynomial ====
    =========================================
    =========================================
    """);
        x_min = 3.7079018462323194
        p = lambda x: (x+8)*(x+6)*(x-2)*(x-5)/100
        lo = 0
        hi = 6

    ## NB: it is so flat at the bottom for our quadratic, we must scale up to succeed, and reduce tigher tolerances
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
            assert x0 < x_min and x_min < x2

##----------------------------------------------------------------

def test_problem_3():

    ## ensure we can call it multiple times
    for lather_rinse_repeat in range(3):

        items = []
        dut.problem_3_fast_avg_init()
        assert 0 == dut.problem_3_fast_avg_get()

        for item in ( i*2 - 41 for i in range(20) ):
            items.append(item)
            dut.problem_3_fast_avg_add(item)
            want = sum(items)/len(items)
            have = dut.problem_3_fast_avg_get()
            assert abs(have-want) < 1e-13
        
##----------------------------------------------------------------

def test_problem_4():

    ## make sure we got the right f
    want_f = lambda x: scale*(x*math.log2(x)) + offset
    have_f = lambda x: dut.problem_4_f(x, scale, offset)
    for scale in (10**d for d in range(-3,3)):
        for offset in range(-200,201,20):
            for n in range (1,20):
                if 0: n = float(n)              # too defensive
                want_y = want_f(n)
                have_y = have_f(n)
                assert abs(want_y - have_y) < 1e-13

    scale,offset = dut.problem_4_get_constants()
    f = have_f
    g = dut.problem_4_g

    ## make sure we got the right relationships with f and g before and after the crossover N

    N = dut.PROBLEM_4_BREAKPOINT

    for n in range(1,N+1):
        if 0: n = float(n)                      # too defensive
        if n < N: assert f(n) > g(n)
        assert f(n) < f(n+1)
        assert g(n) < g(n+1)

    for n in range(N+1,N*3):
        if 0: n = float(n)                      # too defensive
        assert f(n) < g(n)
        assert f(n) < f(n+1)
        assert g(n) < g(n+1)

##[]##
