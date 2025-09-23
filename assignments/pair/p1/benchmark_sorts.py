"""================================================================

Assignment Description

    Implement selection_sort(), insertion_sort(), and bubble_sort();
    compare their performance characteristics; use CLEAN working code.

    Instrument your code to capture the number of data elements scanned
    and the number of swaps performed for each sort.

    Note that each sort is an *inplace* sort.

    Only replace the code between the markers 

        ## vvvv student code goes goes BELOW vvvv ##
        ...   
        ## ^^^^ student code goes goes ABOVE ^^^^ ##

    Leave the rest of the code intact.  Really.  That code runs multiple
    trials, computes the statistics, and graphs the results.

    * you may define your own functions
    * do not use any Python sort() methods
    * do not import or use any Python modules or packages
    * you are welcome to include *disabled* debugging code
    *     even your debugging code should be *clean enough*
    * do not produce extraneous output

    Run the program, adjusting 

        TRIAL_COUNT
        SIZE_RANGE 

    to generate REALIABLE output:

    * the supplied sorts must be of the right type, and give the right results
    * the estimated expected values is accurate (e.g., CoV <= 3% would be nice)
    *     e.g., if the performance curve is quadratic, one should see a parabola

Note

    I usually try very hard to avoid using global *variables*.  
    It's generally a really bad idea.

    But that would make this quite complicated setup even more
    complicated, and hinder understanding.

    Simplicity, for this starter code, is more important.

    The trial results data format is pretty messy, but I wanted to avoid
    using more complicated machinery like pandas, or spend more time on
    an incidental part of this starter code.

================================================================

"""

print("""
=========================
==== Start of Output ====
=========================
""")

import time
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib
import pprint
import sys
import warnings
import math                     # be explicit -- don't depend on other imports satisfying this dependency

def show_stats(tag, sample):
    """ show the basic sample statistics; return (avg,CoV_SEM) """

    (lo,mid,hi) = np.quantile(sample, [0.25, 0.50, 0.75])
    (min,max) = (float(np.min(sample)),  float(np.max(sample)))
    cnt = len(sample)
    (avg,std) = (float(np.mean(sample)), float(np.std(sample)))

    ## coefficient of variation -- avoid dividing by zero ... and get the right signed value, including case 0/0
    if avg != 0:
        CoV_raw = std/avg *100
    else:
        CoV_raw = 0 if std == 0 else np.sign(std) * math.inf

    ## apply Standard Error of the Mean -- comes from Central Limit Theorem -- we're looking at average of iid
    CoV_SEM = CoV_raw / math.sqrt(cnt)

    print(f'''
---- {tag} ----
{min=:0.3e}
25%={lo:0.3e}
50%={mid:0.3e}
75%={hi:0.3e}
{max=:0.3e}

{cnt=:0.3e}
{avg=:0.3e}
{std=:0.3e}
{CoV_raw=:0.2f}%
{CoV_SEM=:0.2f}%
''', end=None )

    cov_warn = 3                # 3 sigma captures 99.7% of population; at 3% CoV, implies our estimate is within 10%
    if CoV_SEM > cov_warn:
        msg = f"{tag=} {CoV_SEM=} > {cov_warn}%"
        warnings.warn(msg)           # output to stderr
        print(f"UserWarning: {msg}") # output to stdout

    return (avg,CoV_raw)

## enable manual (visual)  inspection of show_stats, and verify the returned value
sample = [ float(i) for i in range(101) ]       # generate some easy to analyze data
ev = show_stats("range(101)", sample)           # and print the statistics of the data
assert 50 == ev[0]

##  ----------------------------------------------------------------

action_result = [];           # global variable used to accumulate action outputs

def time_this(tag, action) -> float:
    """determine how long it took to run action()"""
    start_time = time.time()
    result = action()
    end_time = time.time()
    elapsed_time = end_time - start_time
    if tag: print(f"\n{tag} took={elapsed_time:.6f} seconds")

    action_result.append(result)
    return elapsed_time

def time_trials(action):
    """runs action repeatedly and returns a list of the times taken"""
    tag = "show each trial"
    sample = ([ time_this(tag, action) for i in range(TRIAL_COUNT) ]);
    return sample

##================================================================
##================================================================
##================================================================

##  ----------------------------------------------------------------
##  ----------------------------------------------------------------
##  ----------------------------------------------------------------
## vvvv student code goes goes BELOW vvvv ## --leave this line alone

## PlaceHolderCode ##
TRIAL_COUNT = 2                 # NB: must remain CONSTANT, is integer >= 1

## PlaceHolderCode ##
SIZE_RANGE = [17, 42, 79]       # NB: must remain CONSTANT, is list of positive integers

##  ================================================================
##  NB: comparison_count is the number of DATA comparisions
##      exchange_count   is the number of DATA exchanges (aka swaps)
##  ================================================================

## PlaceHolderCode ##
def selection_sort(data):
    ### REPLACE THESE LINES -- MUST USE OWN SORT
    """ PLACEHOLDER: non-stable sort inplace; return (comparison_count, exchange_count) """
    data.sort()
    n = len(data)
    wiggle = n//10
    n += random.randint(1*wiggle, 2*wiggle)
    return  (n*(n-1)/2,  n)

## PlaceHolderCode ##
def insertion_sort(data):
    ### REPLACE THESE LINES -- MUST USE OWN SORT
    """ PLACEHOLDER: stable sort inplace; return (comparison_count, exchange_count) """
    data.sort()
    n = len(data)
    wiggle = n//10
    n += random.randint(1*wiggle, 2*wiggle)
    return  (n*n/4,  n*(n+1)/4)

## PlaceHolderCode ##
def bubble_sort(data):
    ### REPLACE THESE LINES -- MUST USE OWN SORT
    """ PLACEHOLDER: stable sort inplace; return (comparison_count, exchange_count) """
    data.sort() 
    n = len(data)
    wiggle = n//10
    n += random.randint(1*wiggle, 2*wiggle)
    return (n*n/2, n*n/4)

## ^^^^ student code goes goes ABOVE ^^^^ ## --leave this line alone
##  ----------------------------------------------------------------
##  ----------------------------------------------------------------
##  ----------------------------------------------------------------

if 'IS_VERIFY_TEST_HARNESS' in globals():
    pass
else:
    IS_VERIFY_TEST_HARNESS = '--verify_test_harness' in sys.argv

if IS_VERIFY_TEST_HARNESS:

    print(""" ==== Verifying Test Harness ==== """)
    print(""" ==== Verifying Test Harness ==== """)
    print(""" ==== Verifying Test Harness ==== """)

    import _HIDDEN_benchmark_sorts_config as config_dut
    TRIAL_COUNT = config_dut.TRIAL_COUNT;
    SIZE_RANGE  = config_dut.SIZE_RANGE;

    import _HIDDEN_simple_selection_sort as select_dut
    selection_sort = select_dut.my_sort
    select_dut.IS_VERBOSE_MY_SORT = config_dut.IS_VERBOSE_MY_SORT

    import _HIDDEN_simple_insertion_sort as insert_dut
    insertion_sort = insert_dut.my_sort
    insert_dut.IS_VERBOSE_MY_SORT = config_dut.IS_VERBOSE_MY_SORT

    import _HIDDEN_simple_bubble_sort    as bubble_dut
    bubble_sort    = bubble_dut.my_sort
    bubble_dut.IS_VERBOSE_MY_SORT = config_dut.IS_VERBOSE_MY_SORT

##================================================================
##================================================================
##================================================================

## define MANIFEST CONSTANTS

SELECT = 'select'
INSERT = 'insert'
BUBBLE = 'bubble'

_sortKind = [ INSERT, SELECT, BUBBLE ] # re-ordered so markers on plots come out nicely

sort_map = { SELECT:selection_sort, INSERT:insertion_sort, BUBBLE:bubble_sort }

## define metric as manifest constant to reduce risk of runtime error
## NB: this is the name of the metric, which is also part of the name of the output file

WALLCLOCK       = 'wallClock'
COMPARE         = 'compareCount'
EXCHANGE        = 'exchangeCount'
MEMORYACCESS    = 'accessCount'

_metrics = [ 
    WALLCLOCK    ,
    COMPARE      ,
    EXCHANGE     ,
    MEMORYACCESS ,
]

##  ----------------------------------------------------------------

def is_sorted(data):
    """check to see that incoming data is sorted"""
    have = data[0]
    for item in data:
        if have <= item:
            have = item
        else:
            return False
    return True

def safe_sort(sort, data):
    """ run in-place sort w/ randomized data; return (comparison_count, exchange count) """
    debug = 0

    if debug: print(f"DEBUG: safe_sort prior shuffle {data=}")
    random.shuffle(data)        # shuffle so repeated runs have varying random input
    if debug: print(f"DEBUG: safe_sort after shuffle {data=}")

    result = sort(data)

    if 0:                       # force sort failure to test error detection
        random.shuffle(data)
    if not is_sorted(data):
        raise RuntimeError("resulting data not sorted")
    return result

##  ----------------------------------------------------------------

## limit range of NON-NEGATIVE data values to aid debugging and testing
lo = 0;
hi = 10**5;                     # exclusive upper bound => limit digits --  keep it small to ease debugging

def get_data(size):
    data = [ random.randint(lo,hi) for _ in range(size) ];
    return data;

##  ----------------------------------------------------------------

trial_result = dict()           # { name:(time,compare,exchange) } average values

def run_trials(size):
    """ run the available sorts for the given size, leaving results in trial_result"""
    trial_result.clear();
    data = get_data(size)
    for sort_name in sort_map:
        print(f"==== {sort_name=} {size=}====")
        action_result.clear();
        time_cost = time_trials(lambda: safe_sort(sort_map[sort_name], data));
        if 1: print(f'{action_result=}');
        look_cost = [item[0] for item in action_result]
        swap_cost = [item[1] for item in action_result]

        ev_time = show_stats("time_cost", time_cost)
        ev_look = show_stats("look_cost", look_cost)
        ev_swap = show_stats("swap_cost", swap_cost)

        trial_result[sort_name] = (ev_time, ev_look, ev_swap);
        
sweep_result = dict();          # { size: trial_result }

def run_sweep_sort():
    """ run trials and leave result in global sweep_result """
    sweep_result.clear()
    for size in SIZE_RANGE:
        run_trials(size)
        sweep_result[size] = trial_result.copy() # NB: making a copy is critical!

##----------------------------------------------------------------

def grab_xy(results, metric, kind):
    """ return requested x and y data """
    debug = 0
    is_use_dummy = 0

    if debug: print(f"DEBUG: grab_xy({results=}, {metric=}, {kind=}) starting ...")

    if is_use_dummy:
        x = SIZE_RANGE
        y = np.array(SIZE_RANGE)**2;

        ## jitter x to distinguish if overlap; AI was helpful here ;-)
        ## better would be to jitter y, but good enough is good enough
        x = np.array(x).astype(float)
        x += 0.25 * _sortKind.index(kind)
        x = x.tolist()

    else:
        x = []
        y = []
        for size in SIZE_RANGE:
            _cost = results[size][kind]
            if debug: print(f"{_cost=}")

            if   WALLCLOCK    == metric: cost = _cost[0]
            elif COMPARE      == metric: cost = _cost[1]
            elif EXCHANGE     == metric: cost = _cost[2]
            elif MEMORYACCESS == metric: cost = _cost[1]+_cost[2]
            else:                        assert "unexpected metric"

            x.append(size)
            y.append(cost[0])   # take just the avg from (avg,CoV)

    if debug: print(f"DEBUG: {x=} {y=}");
    if debug: print(f"DEBUG: ... grab_xy(results, {metric=}, {kind=}) finished")

    return (x,y)
    
def plot_one_graph(results, metric):
    """plot a graph and save the result"""
    debug = 0

    if debug: print(f"DEBUG: plot_one_graph {metric=}")

    plt.figure(figsize=(7,9.5)); # portrait
    plt.rcParams['font.size'] = 14
    plt.rcParams['axes.labelsize'] = 16 
    plt.rcParams['xtick.labelsize'] = 12
    plt.rcParams['ytick.labelsize'] = 12
    plt.rcParams['axes.titlesize'] = 18

    for spot in range(len(_sortKind)):
        kind = _sortKind[spot]
        (x, y) = grab_xy(results, metric, kind)
        plt.plot(x, y, label=kind, marker=spot+8, ms=10, mew=2)

    plt.xlabel("problem size");

    ylabel = f"{metric}"
    if metric in [WALLCLOCK]: ylabel += " seconds"
    plt.ylabel(ylabel)

    plt.legend(loc="upper center");
    plt.title("Simulation results: average " + metric);

    plt.savefig("compare_simple_sorts_"+metric+".png", bbox_inches='tight');
    plt.pause(0.001);       # trick to enable non-blocking display of plots

def plot_trial_results(results):
    """plot trial results in separate graphs"""

    plt.close('all')

    plot_one_graph(results, WALLCLOCK    )
    plot_one_graph(results, COMPARE      )
    plot_one_graph(results, EXCHANGE     )
    plot_one_graph(results, MEMORYACCESS )

##----------------------------------------------------------------

def get_trial_results(is_run_trials = True):
    """return results from running trials or use fake data"""
    verbose = 0
    if is_run_trials:
        run_sweep_sort()
        results = sweep_result
        print("results=")
        pprint.pprint(results)
    else:
        ## might not work any longer -- this is a snapshot
        ## we vary the info we track -- here's an illustration
        results = (
            {17: {'bubble': (2.0265579223632812e-05, 173.1, 86.55),
                  'insert': (1.5354156494140626e-05, 86.55, 91.2),
                  'select': (2.0074844360351563e-05, 156.6, 18.2)},
             42: {'bubble': (3.0946731567382815e-05, 1162.9, 581.45),
                  'insert': (3.123283386230469e-05, 557.2, 569.0),
                  'select': (3.399848937988281e-05, 1138.2, 48.2)},
             79: {'bubble': (4.668235778808594e-05, 4033.9, 2016.95),
                  'insert': (5.0687789916992186e-05, 1945.15, 1967.2),
                  'select': (6.794929504394531e-05, 3883.6, 88.6)}}
        )

    if verbose: print(f'{results=}')
    return results

def clear():
    ## name inspired by clear(1) - clear the terminal screen
    """helper function to close all our matplotlib.pyplot windows"""
    plt.close('all')

def clean():
    ## name inspired by `clean', a common Makefile target
    """helper function to clean out our _HIDDEN_ modules"""
    del sys.modules['_HIDDEN_benchmark_sorts_config']
    del sys.modules['_HIDDEN_simple_selection_sort']  
    del sys.modules['_HIDDEN_simple_insertion_sort']  
    del sys.modules['_HIDDEN_simple_bubble_sort']     
    
def main():
    results = get_trial_results()
    plot_trial_results(results)

    if IS_VERIFY_TEST_HARNESS:
        print()
        print(""" ==== Verifying Test Harness ==== """)
        print(""" ==== Verifying Test Harness ==== """)
        print(""" ==== Verifying Test Harness ==== """)

main()

print('''
===============
==== [QED] ====
===============
''')

#[]#
