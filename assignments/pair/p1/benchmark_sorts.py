"""================================================================

Assignment Description

    Implement selection_sort(), insertion_sort(), and bubble_sort();
    compare their performance characteristics; use CLEAN working code.

    Instrument your code to capture the number of data elements scanned
    and the number of swaps performed for each sort.

    Note that each sort is an *inplace* STABLE selection sort.

    Leave the boiler plate Start of Output and QED intact.  Replace
    places marked with ## PlaceHolderCode ## with your code.  Remove all
    code you don't use.

    * you may define your own functions
    * do not use any Python sort() methods
    * do not import any additional Python modules or packages
    * do not include any debugging code 
    * do not produce extraneous output

    I'll provide routines to run multiple trials, compute the
    statistics, and graph the results.

    Run the sorts for a range of input sizes and generate the resulting
    performance curves.  Choose a range of sizes to generate a reliable
    curve -- if it's quadratic, you should see a parabola.

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

def show_stats(sample):
    """ show the basic sample statistics; return the average """
    (lo,mid,hi) = np.quantile(sample, [0.25, 0.50, 0.75])
    (min,max) = (float(np.min(sample)),  float(np.max(sample)))
    (avg,std) = (float(np.mean(sample)), float(np.std(sample)))
    CoV = std/avg *100          # coefficient of variation
    cnt = len(sample)
    print(f'''
{min=:0.3e}
25%={lo:0.3e}
50%={mid:0.3e}
75%={hi:0.3e}
{max=:0.3e}

{cnt=:0.3e}
{avg=:0.3e}
{std=:0.3e}
{CoV=:0.2f}%
''', end=None )

if 0:
    ## smoketest show_stats
    sample = [ float(i) for i in range(101) ] # generate some easy to analyze data
    show_stats(sample)                        # and print the statistics of the data

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
    repeat = 5
    tag = "show each trial"

    sample = ([ time_this(tag, action) for i in range(repeat) ]);

    if 1: print(f'{sample=}')
    if 1:show_stats(sample)

    return sample

##  ----------------------------------------------------------------

## PlaceHolderCode ##
size_range = [17, 42, 79]

## PlaceHolderCode ##
def selection_sort(data):
    """ stable sort inplace; return (comparison_count, exchange_count) """
    n = len(data)
    return  (n*(n-1)/2,  n)

## PlaceHolderCode ##
def insertion_sort(data):
    """ stable sort inplace; return (comparison_count, exchange_count) """
    n = len(data)
    return  (n*n/4,  n*(n+1)/4)

## PlaceHolderCode ##
def bubble_sort(data):
    """ stable sort inplace; return (comparison_count, exchange_count) """
    n = len(data)
    return (n*n/2, n*n/4)

##  ----------------------------------------------------------------

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

def safe_sort(sort, data):
    """ run in-place stable sort with few side effects; return (comparison_count, exchange count) """
    copy = list(data)           # make a copy to avoid updating input so we can run repeated trials
    return sort(copy)

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
        action_result.clear();
        time_used = time_trials(lambda: safe_sort(sort_map[sort_name], data));
        if 1: print(f'{action_result=}');
        compare_count =  [item[0] for item in action_result]
        exchange_count = [item[1] for item in action_result]
        wall_used = float(np.array(time_used).mean())
        comp_used = float(np.array(compare_count).mean())
        exch_used = float(np.array(exchange_count).mean())
        trial_result[sort_name] = (wall_used, comp_used, exch_used);
        
sweep_result = dict();          # { size: trial_result }

def run_sweep_sort():
    """ run trials and leave result in global sweep_result """
    sweep_result.clear()
    for size in size_range:
        run_trials(size)
        sweep_result[size] = trial_result.copy() # NB: making a copy is critical!

##----------------------------------------------------------------

def grab_xy(results, metric, kind):
    """ return requested x and y data """
    debug = 0
    is_use_dummy = 0

    if debug: print(f"DEBUG: grab_xy({results=}, {metric=}, {kind=}) starting ...")

    if is_use_dummy:
        x = size_range
        y = np.array(size_range)**2;

        ## jitter x to distinguish if overlap; AI was helpful here ;-)
        ## better would be to jitter y, but good enough is good enough
        x = np.array(x).astype(float)
        x += 0.25 * _sortKind.index(kind)
        x = x.tolist()

    else:
        x = []
        y = []
        for size in size_range:
            _cost = results[size][kind]
            if debug: print(f"{_cost=}")

            if   WALLCLOCK    == metric: cost = _cost[0]
            elif COMPARE      == metric: cost = _cost[1]
            elif EXCHANGE     == metric: cost = _cost[2]
            elif MEMORYACCESS == metric: cost = _cost[1]+_cost[2]
            else:                        assert "unexpected metric"

            x.append(size)
            y.append(cost)

    if debug: print(f"DEBUG: {x=} {y=}");

    if debug: print(f"DEBUG: ... grab_xy(results, {metric=}, {kind=}) finished")
    return (x,y)
    
def plot_one_graph(results, metric):
    """plot a graph and save the result"""
    debug = 0

    if debug: print(f"DEBUG: plot_one_graph {metric=}")

    plt.figure(figsize=(7,9.5)); # portrait
    plt.rcParams['font.size'] = 14  # Change to your desired size
    plt.rcParams['axes.labelsize'] = 16  # Axis labels
    plt.rcParams['xtick.labelsize'] = 12  # X-axis tick labels
    plt.rcParams['ytick.labelsize'] = 12  # Y-axis tick labels
    plt.rcParams['axes.titlesize'] = 18  # Title size    

    for spot in range(len(_sortKind)):
        kind = _sortKind[spot]
        (x, y) = grab_xy(results, metric, kind)
        plt.plot(x, y, label=kind, marker=spot+8, ms=10, mew=2)

    plt.xlabel("problem size");
    plt.ylabel(f"{metric}");              # demo f-string not used in print()
    plt.legend(loc="upper center");
    plt.title("Simulation results: expected " + metric);

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
    else:
        ## no longer works -- we've increased the size_range
        results = {
         17: {
            'select': (4.00543212890625e-06, 136.0, 17.0),
            'insert': (6.4373016357421875e-06, 72.25, 72.25),
            'bubble': (8.726119995117188e-06, 144.5, 72.25)},
         42: {
             'select': (1.659393310546875e-05, 861.0, 42.0),
             'insert': (5.340576171875e-06, 441.0, 441.0),
             'bubble': (4.9591064453125e-06, 882.0, 441.0)}
        }

    if verbose: print(f'{results=}')
    return results

def main():
    results = get_trial_results()
    plot_trial_results(results)

main()

print('''
===============
==== [QED] ====
===============
''')

#[]#
