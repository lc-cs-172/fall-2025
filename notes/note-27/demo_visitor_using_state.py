"""Purpose: Show how to create a visitor function that uses local, not global, state"""

def starting(msg):
    print('\n' + msg)

starting('''
====================
==== here we go ====
====================
''')

data = range(8)

def visit(sequence, visitor):
    for item in sequence:
        visitor(item)

##================

def demo_visit_using_print():
    starting('==== demo_visit_using_print ====')
    visit(data, print)

##================

"""Demo simple UGLY visitor using global variables"""

suv_avg_count = None
suv_avg_total = None

def suv_setup():
    global suv_avg_count, suv_avg_total
    suv_avg_count = 0
    suv_avg_total = 0

def suv_visitor(item):
    global suv_avg_count, suv_avg_total
    suv_avg_count += 1
    suv_avg_total += item

def suv_fetch():
    global suv_avg_count, suv_avg_total
    return suv_avg_total / suv_avg_count
    
def suv_print():
    suv_avg_fetch = suv_fetch()
    print(f'{suv_avg_count=} {suv_avg_total=} {suv_avg_fetch=}')    

def demo_simple_ugly_visitor():
    starting('==== demo_simple_ugly_visitor ====')
    suv_setup()
    visit(data, suv_visitor)
    suv_print()

##================

"""We define an object as a callable to allow our visitor function to have local state and expose results"""

class Dynamic_Mean:

    ## Define and initialize all our attributes.
    ## I really like to see all the object attributes defined in one place
    ## so I know what all of them are.

    ## I had marked these attributes as 'private' with a leading underbar,
    ## but I'm expected the user to reach in and read their values,
    ## so that makes them public.  Too bad I can't make 'em readonly.

    count = 0
    total = 0
    mean  = 0

    ## NB: __init__ not needed!
    ##     we let Python automatically initialize our object attributes from the class attributes
    ##     we also support reset, which will set them to 0

    def __repr__(self):
        return f'Dynamic_Mean({self.count=} {self.total=} {self.mean=})'

    def __call__(self, item):
        self.count += 1
        self.total += item
        self.mean = self.total/self.count

    def reset(self):
        self.count = 0
        self.total = 0
        self.mean  = 0

def demo_visit_using_object():
    starting('==== demo_visit_using_object ====')

    trio = range(1,4)

    ## using v1 and v2 to ensure that different objects stay separated
    
    def emit_both():
        ## since we do not change them, v1 and v2 are our outer variables, not local variables for this function
        print(f'{v1=!r}') # FYI: !r means use the __repr__ string representation
        print(f'{v2=!s}') # FYI: !s means use the __str__ string representation which defaults to __repr__

    v1 = Dynamic_Mean()
    v2 = Dynamic_Mean()
    print('create both objects')
    emit_both()

    print('visit(data, v1)')
    visit(data, v1)
    emit_both()

    print('visit(trio, v2)')
    visit(trio, v2)
    emit_both()

    print('v1.reset()')
    v1.reset()
    emit_both()

    print('visit(data,v1)')
    visit(data, v1)
    emit_both()
    print('visit(data,v1)')
    visit(data, v1)
    emit_both()
    
##================
##================
##================

##================================================================
##================================================================
## Q/ How can we return a result from a visitor
##    besides in global variables or an object?
## A/ See below.
##----------------------------------------------------------------
## What is below here is too  complex for us right now
## -- but it's here for me to maybe share with you later.
## NB: These techniques are not something I would ordinarily use for this.
##----------------------------------------------------------------
## I really prefer an object to encapulate local state.
## I really prefer an object to encapulate local state.
## I really prefer an object to encapulate local state.
##----------------------------------------------------------------
##================================================================
##================================================================

##================

"""We can define a local function using local variables to allow our visitor function to access local state"""

def demo_visit_using_local():
    starting('==== demo_visit_using_local ====')

    count = 0
    total = 0
    mean = 0

    ## NB: this is a 'one-shot' function -- we didn't provide a way to reset local state
    def mean_visitor(item):
        nonlocal count, total, mean
        count += 1
        total += item
        mean = total/count

    visit(data, mean_visitor)
    print(f'{count=} {total=} {mean=}')

##================

"""We manufacture a function from a factory with local storage, but are unable to RETURN the result"""

def demo_visit_using_factory():
    starting('==== demo_visit_using_factory ====')

    def make_noisy_visitor():
        count = 0
        total = 0
        mean = 0
        def mean_visitor(item):
            nonlocal count, total, mean
            count += 1
            total += item
            mean = total/count
            print(f'{count=} {total=} {mean=}')

        return mean_visitor

    visitor = make_noisy_visitor()
    visit(data, visitor)

##================

"""We manufacture a function using a factory, and give it the local storage to use.
This lets us accumlate and RETURN the overall result from the visitor."""

def make_mean_visitor_given_dict(d):
    'NB: d is a dictionary, and is our storage'
    assert type(d) == dict
    d.clear()
    d['count'] = 0
    d['total'] = 0
    d['mean'] = 0
    def mean_visitor(item):
        ## NB: `nonlocal d` not needed ;-) -- why not? 
        d['count'] += 1
        d['total'] += item
        d['mean'] = d['total']/d['count']
    return mean_visitor

def demo_visit_given_dict():
    starting('==== demo_visit_given_dict ====')
    storage = {}

    visitor = make_mean_visitor_given_dict(storage)
    visit(data, visitor)
    print(storage)

    ## demo if avoid reset -- keeps accumulating
    visit(data, visitor)
    print(storage)

    visitor = make_mean_visitor_given_dict(storage)
    visit(data, visitor)
    print(storage)

##================

"""We manufacture a function using a factory, and have it return the local storage it created and will use.
This lets us accumlate and RETURN the overall result from the visitor."""

def make_mean_visitor_fresh_dict():
    'Return (visitor,dictionary)'
    d = {}
    d['count'] = 0
    d['total'] = 0
    d['mean'] = 0
    def mean_visitor(item):
        ## NB: `nonlocal d` not needed ;-) -- why not? 
        d['count'] += 1
        d['total'] += item
        d['mean'] = d['total']/d['count']
    return (mean_visitor,d)

def demo_visit_fresh_dict():
    starting('==== demo_visit_fresh_dict ====')

    visitor,storage = make_mean_visitor_fresh_dict()
    visit(data, visitor)
    print(storage)

    ## demo if avoid reset -- keeps accumulating
    visit(data, visitor)
    print(storage)

    visitor,new_storage = make_mean_visitor_fresh_dict()
    assert new_storage is not storage
    visit(data, visitor)
    print(new_storage)

##================

demo_visit_using_print()
demo_simple_ugly_visitor()
demo_visit_using_object()

demo_visit_using_local()
demo_visit_using_factory()
demo_visit_given_dict()
demo_visit_fresh_dict()

[]
