print('\n==== Purpose: demo "simple" Python iterators ====')

"""
                                                                               
 ######  #    #  #####      #     ####   #    #  #    #  ######  #    #   #####
 #       ##   #  #    #     #    #    #  #    #  ##  ##  #       ##   #     #  
 #####   # #  #  #    #     #    #       ######  # ## #  #####   # #  #     #  
 #       #  # #  #####      #    #       #    #  #    #  #       #  # #     #  
 #       #   ##  #   #      #    #    #  #    #  #    #  #       #   ##     #  
 ######  #    #  #    #     #     ####   #    #  #    #  ######  #    #     #  
                                                                               

You are not responsible for knowing the details of this demo code.

It is enrichment.  You need to be exposed, you need to know it exists,
but you don't need to know it cold.  

================================================================
You will be tested on iterators and yield.
You won't be tested on the gory details of iter() and __next__().
================================================================

You am not being trained as Python language lawyers
-- you are being taught computer science.

Python iteration semantics are pretty complicated on first exposure --
there are lots of important tiny details --
what's a function, what's an iterator, what's a callable,
there are multiple flavors of iter(),
there are sentinels vs. exceptions to terminate iteration ...
and there are functions that return functions,
there are closures.

Python is still growing and changing for almost 35 years.
Python needs it.

It's more than we need.  We'll stick to basics.

"""

master = [3, 2, 1]

default_if_done = 'and then there were none'

def make_iterator():
    "NB: this is not an iterator -- it returns an iterator"
    yield 3
    yield 2
    yield 1

##----------------

## countdown is a Noun  (object)
## count down is a Verb (action)

countdown_counter = None
countdown_sentinel = 'Give up, Dorathy'

def countdown_reset(start_at):
    "initialize our countdown counter with 'start_at', the next value returned"
    global countdown_counter
    countdown_counter = start_at +1     # bump by 1 since we decrement before return

def count_down():
    'Purpose: callable usable as an iterator -- counts down to 1, does not return 0'

    ##================================================================
    ## NB: This function deliberately has a bug.
    ##================================================================

    global countdown_counter

    if countdown_counter:
        countdown_counter -= 1
        return countdown_counter

    return countdown_sentinel

##----------------
## Q/ Wouldn't it be nice to use an object for our count_down?
## 
## A/ Yes!
## - Avoid globals (which you might forget to reset)
## - Simplify naming -- avoid cluttering prefix 'countdown_'
##----------------

def demo_builtin_iter():
    one_by_one = iter(master)
    for item in master:
        assert item == next(one_by_one)
    if 0:
        ## raises exception
        item = next(one_by_one)
    else:
        assert default_if_done == next(one_by_one, default_if_done)
    print('SUCCESS')
        
def demo_generator():
    one_by_one = make_iterator()
    for item in master:
        assert item == next(one_by_one)
    if 0:
        ## will raise exception StopIteration
        item = next(one_by_one)
    else:
        assert default_if_done == next(one_by_one, default_if_done)
    print('SUCCESS')

def demo_builtin_iter_alt():
    countdown_reset(3)
    one_by_one = iter(count_down, countdown_sentinel)
    for item in master:
        lump = next(one_by_one)
        if 1: print('DEBUG: item:', item, 'lump:', lump)
        assert item == lump
    if 0:
        ## Q/ raises exception -- I thought -- what's up this this?
        lump = next(one_by_one)
        if 1: print('DEBUG: item:', item, 'lump:', lump)
        ## A/ my count_down routine is faulty!!
        lump = next(one_by_one)
        if 1: print('DEBUG: item:', item, 'lump:', lump)
    else:
        if 1:                                   # handle our bug
            lump = next(one_by_one)
            assert lump == 0
        if 0:
            ## we expect an exception -- let us see if we got one
            lump = next(one_by_one)  
        else:

            ## show that sentinel is OK, and that is it ours, not the iterators
            sentinel = 'Q/ Is it legal to supply a new sentinel?'
            what_we_got = next(one_by_one, sentinel)
            if 1: print('DEBUG: what_we_got:', what_we_got)
            assert sentinel == what_we_got

            ## do we still see the well ran dry, or will this do something else?
            what_we_got = next(one_by_one, sentinel)
            if 1: print('DEBUG: what_we_got:', what_we_got)
            assert sentinel == what_we_got

    print('SUCCESS')
        
if 1: demo_builtin_iter()
if 1: demo_generator()
if 1: demo_builtin_iter_alt()


[]        
