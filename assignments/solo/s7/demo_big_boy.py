print('''
==== demo cost compare of insert_sort vs. merge_sort ====
''')

import time
import numpy as np
import statistics
import show_stats as shst

from _HIDDEN_insertion_sort import insertion_sort as insertion_sort
from _HIDDEN_merge_sort_dnc import merge_sort_dnc as merge_sort_dnc

TRIALS = 3

def time_action(tag, action, data) -> float:
    size = len(data)
    times = []
    for trial in range(TRIALS):
        ## we have to make copies -- action may modify data in-place
        my_data = data.copy()
        head = time.perf_counter()
        action(my_data)
        tail = time.perf_counter()
        used = tail - head
        times.append(used)
        print('trial', trial, 'tag', tag, 'size', size, 'used', used);
    shst.show_stats(tag, times)
    print()
    return statistics.median(times)

def demo_sort_cost():
    hand = np.random.randint(0,2**20,int(5e3))
    data = list(hand)
    insertion_used = time_action('insertion_sort', insertion_sort, data)
    merge_dnc_used = time_action('merge_sort_dnc', merge_sort_dnc, data)
    better = insertion_used/merge_dnc_used
    print(f'==== {insertion_used=:.02e} {merge_dnc_used=:.02e} {better=:.02f} ====\n')

def main():
    demo_sort_cost()

if '__main__' == __name__:
    main()

[]
