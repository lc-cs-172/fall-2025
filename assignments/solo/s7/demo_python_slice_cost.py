print('''

====================
==== ENRICHMENT ====
====================

==== demo cost of Python slice ====
''')

import time
import show_stats as shst
import statistics as stat

def JPS_merge(run1, run2):
    """ merge two sorted segments into one larger sorted segment, returning the results """
    assert run1
    assert run2
    ## NB: clever indexing -- use spot (-size) to access next element,
    ##     starting from the front,
    ##     and increase spot until 0 (i.e., all processed)
    result = []
    spot1 = -len(run1)
    spot2 = -len(run2)
    while spot1 and spot2:
        if run1[spot1] <= run2[spot2]:
            result.append(run1[spot1])
            spot1 += 1
            if not spot1:
                result += run2[spot2:]
        else:
            result.append(run2[spot2])
            spot2 += 1
            if not spot2:
                result += run1[spot1:]
    return result

def pop_merge(run1, run2):
    """ merge two sorted segments into one larger sorted segment, returning the results """
    assert run1
    assert run2
    ## NB: using straight-forward pop -- let us see what is the cost
    result = []
    while 1:
        if run1[0] <= run2[0]:
            result.append(run1.pop(0))
            if not len(run1): break
        else:
            result.append(run2.pop(0))
            if not len(run2): break
    result.extend(run1)
    result.extend(run2)
    return result

def ALT_merge(list_1, list_2):
    result = []
    # Combs through the two lists and appends the smaller element to the result list each time. This loop ends when one
    # of the lists is empty.
    while list_1 and list_2:
        if list_1[0] <= list_2[0]:
            result.append(list_1[0])
            list_1[:] = list_1[1:]
        elif list_1[0] > list_2[0]:
            result.append(list_2[0])
            list_2[:] = list_2[1:]
    # If one of the lists is empty and the other is not after the above while loop runs, then we know that all elements
    # of the non-empty list are greater than all elements of the result list. Thus, we can just tack the remaining
    # elements onto the end of the result list.
    if list_1:
        result += list_1
    elif list_2:
        result += list_2
    return result

TRIALS = 3

def time_merge(tag, merge, run1, run2) -> float:
    size = len(run1) + len(run2)
    times = []
    for trial in range(TRIALS):
        ## we have to make copies -- ALT_merge modifies the input
        my_run1 = run1.copy()
        my_run2 = run2.copy()
        head = time.perf_counter()
        result = merge(my_run1, my_run2)
        tail = time.perf_counter()
        assert result == sorted(result)
        used = tail - head
        times.append(used)
        print('trial', trial, 'tag', tag, 'size', size, 'used', used);
    if 0: shst.show_stats(tag, times)
    print()
    return statistics.median(times)

def demo_slice_cost():
    for size in [10_000, 20_000, 30_000]:
        run1 = [i for i in range(1, size+1, 2) ]
        run2 = [j for j in range(2, size+1, 2) ]
        assert run1 == sorted(run1)
        assert run2 == sorted(run2)
        jps_used = time_merge('JPS', JPS_merge, run1, run2)
        alt_used = time_merge('ALT', ALT_merge, run1, run2)
        pop_used = time_merge('pop', pop_merge, run1, run2)
        worse_alt_pop = alt_used/pop_used
        worse_pop_jps = pop_used/jps_used
        worse_alt_jps = alt_used/jps_used
        print('================================================================')
        print(f'{size=} {jps_used=:.3e} {alt_used=:.3e} {pop_used=:.3e}')
        print(f'{worse_alt_pop=:.1f} {worse_pop_jps=:.1f} {worse_alt_jps=:.1f}');
        print('================================================================')
              
def main():
    demo_slice_cost()

if '__main__' == __name__:
    main()

[]
