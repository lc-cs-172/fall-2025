print('\n==== Purpose: demo simple Python iterators ====')

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
    one_by_one = iter(count_down, count_down_sentinel)
    for item in master:
        lump = next(one_by_one)
        if 1: print('DEBUG: item:', item, 'lump:', lump)
        assert item == lump
    if 1:
        ## raises exception
        item = next(one_by_one)
    else:
        assert sentinel == next(one_by_one, sentinel)
    print('SUCCESS')
        
if 1: demo_builtin_iter()
if 1: demo_generator()
if 1: demo_builtin_iter_alt()


[]        
    
    
