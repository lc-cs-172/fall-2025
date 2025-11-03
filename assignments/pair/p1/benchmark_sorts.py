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

## try to ensure all the warnings are displayed in vs code -- some places yes, some places no with or without this
warnings.simplefilter("always")

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
## vvvv student code goes goes BELOW vvvv -- leave this line alone
##================================================================
##================================================================

## PlaceHolderCode ##
##----------------------------------------------------------------
## This value determines the number of times the sort of the given size is run.

## Since the metrics can depend on the input data, we have to run
## multiple trials and average them to get the expected value.

## That is, just like we need to flip a coin a number of times to see if
## it's fair, we need to run sorts with metrics dependent on input data
## to determine its expected (average) cost.
## ----------------------------------------------------------------
TRIAL_COUNT = 2                 # NB: must remain CONSTANT, is integer >= 1

## PlaceHolderCode ##
##----------------------------------------------------------------
## This value determines the various sizes of the data that gets sorted.
## Larger sizes take longer, but usually give more accurate results.
##----------------------------------------------------------------
SIZE_RANGE = [17, 42, 79]       # NB: must remain CONSTANT, is list of positive integers

##  ================================================================
##  NB: comparison_count is the number of DATA comparisions
##      exchange_count   is the number of DATA exchanges (aka swaps)
##  ================================================================

##----------------------------------------------------------------
## These are DUMMY sort routines used to verify the test harness.
## They are NOT NECESSARILY ACCURATE wrt/ metrics returned!
## You need to replace them with your own instrumented code.
##----------------------------------------------------------------
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

##================================================================
##================================================================
## ^^^^ student code goes goes ABOVE ^^^^ -- leave this line alone
##================================================================
##================================================================

## provide dummy routine to satisfy the test fixture
def mystery_sort(data):
    data.sort()
    return(0,0)

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

    ## FYI: vscode likes to complain about this one ...
    ##
    import _HIDDEN_simple_mystery_sort    as mystery_dut
    mystery_sort    = mystery_dut.my_sort
    mystery_dut.IS_VERBOSE_MY_SORT = config_dut.IS_VERBOSE_MY_SORT

## define MANIFEST CONSTANTS

SELECT = 'select'
INSERT = 'insert'
BUBBLE = 'bubble'
MYSTERY = 'mystery'

_sortKind = [ INSERT, SELECT, BUBBLE, MYSTERY ] # re-ordered so markers on plots come out nicely

sort_map = { SELECT:selection_sort, INSERT:insertion_sort, BUBBLE:bubble_sort, MYSTERY:mystery_sort }

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
            elif MEMORYACCESS == metric: cost = (_cost[1][0]+_cost[2][0],0) # make fake tuple -- tuple + concatenates!!!
            else: 
                ## quiet Pylance complaint by assigning dummy value we should never use
                cost = (0,0)    
                assert "unexpected metric"

            x.append(size)
            y.append(cost[0])   # take just the avg from (avg,CoV)

    if debug: print(f"DEBUG: {x=} {y=}");
    if debug: print(f"DEBUG: ... grab_xy(results, {metric=}, {kind=}) finished")

    return (x,y)
    
def plot_one_graph(results, metric):
    """plot a graph and save the result"""
    debug = 1

    if debug: print(f"\n\nDEBUG: plot_one_graph {metric=}")

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
        if debug: print(f'DEBUG: plt.plot({x=}, {y=}, label={kind})')

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
        ## we keep refining the info we track -- here's an illustration
        ## FYI: it's (avg,CoV) for (time, look, swap)
        results={
         17: {'bubble': ((2.765655517578125e-05, 13.793103448275861),
                         (171.25, 5.401459854014599),
                         (85.625, 5.401459854014599)),
              'insert': ((2.8252601623535156e-05, 18.143459915611814),
                         (85.625, 5.401459854014599),
                         (90.25, 5.263157894736842)),
              'mystery': ((2.47955322265625e-05, 10.576923076923077),
                          (0.0, 0),
                          (0.0, 0)),
              'select': ((2.9325485229492188e-05, 20.32520325203252),
                         (153.0, 0.0),
                         (18.0, 0.0))},

         42: {'bubble': ((4.982948303222656e-05, 4.30622009569378),
                         (1081.25, 2.1502890173410405),
                         (540.625, 2.1502890173410405)),
              'insert': ((5.125999450683594e-05, 3.255813953488372),
                         (540.625, 2.1502890173410405),
                         (552.25, 2.127659574468085)),
              'mystery': ((4.57763671875e-05, 6.25), (0.0, 0), (0.0, 0)),
              'select': ((4.887580871582031e-05, 5.365853658536586),
                         (1058.0, 2.1739130434782608),
                         (46.5, 1.0752688172043012))},

         79: {'bubble': ((8.594989776611328e-05, 4.0221914008321775),
                         (4232.5, 2.173656231541642),
                         (2116.25, 2.173656231541642)),
              'insert': ((8.928775787353516e-05, 3.337783711615487),
                         (1981.25, 4.492113564668769),
                         (2003.5, 4.4671824307461945)),
              'mystery': ((8.20159912109375e-05, 3.1976744186046515),
                          (0.0, 0),
                          (0.0, 0)),
              'select': ((8.487701416015625e-05, 2.8089887640449436),
                         (4186.5, 2.185596560372626),
                         (92.0, 1.0869565217391304))}
        }

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
