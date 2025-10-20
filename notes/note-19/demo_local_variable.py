size = 8

print('''
================
ready, set, go!!
================
''');

""" 

*** Google AI will contradict itself ***

Q/ in python, do we ever create a local variable by assignment in a
function, but are able to reference the global variable of the same name
prior to the assignment?

A/ No, in Python, if a variable is assigned a value anywhere within a
function's body, that variable is considered local to the function by
default, even if a global variable with the same name exists. This is
known as shadowing.

*** Google AI gets it wrong!!! ***

Q/ in any programming language, do we ever create a local variable by
assignment in a function, but are able to reference the global variable
of the same name prior to the assignment?

A/ In Python, if you assign a value to a variable within a function,
that variable is by default considered local to the function. However,
if you want to reference a global variable with the same name before
that local assignment, you can.

================================================================

 -------------------
*optional enrichment*
 -------------------

What's stated above is not the truth, the whole truth, and nothing but
the truth[*].

Python seems pretty simple from 30,000 foot view (e.g., everything
is an object), but it is quite tricky deep down and up close and
personal (e.g., references are actually quite special, small integers
get interned), and it's even more subtle than what's described here --

This is one of those situations where the abolute truth is [much] more
complicated than the what-most-folks-understand-and-works-in-most-cases.

  Recall earlier example:

    Q/ How to start the car?
    A/ Push the start button (or turn the key).

    More complicated, more complete answer:
    if the battery is charged,
    if there's gas in the tank,
    if the battery is connected,
    if the fuel line is not clogged (frozen fuel line in NJ winter),
    if the fuse isn't blown,
    if ...

[*] "The Truth, the Whole Truth and Nothing but the Truth" -- 

    The formula of the oath as "the whole truth and nothing but the
    truth" originated in the common law jurisdiction of medieval
    England, ...

    https://www.gla.ac.uk/schools/humanities/research/philosophyresearch/researchprojects/thewholetruth/totalityandlegaltheory/

"""

global_var = "I am global via Google"
def try_read_is_global_write_makes_local():
    print(f"Inside function, before local assignment: {global_var}")
    global_var = "I am local"
    print(f"Inside function, after local assignment: {global_var}")
if 0: try_read_is_global_write_makes_local()
print(f"Outside function: {global_var}")

global_var_alt = "I am an alternate global variable that will not be accessed via an f-string"
def try_alt_read_is_global_write_makes_local():
    print("Inside function, before local assignment:", global_var_alt)
    global_var_alt = "I am local"
    print("Inside function, after local assignment:", global_var_alt)
if 0: try_alt_read_is_global_write_makes_local()
print(f"Outside function: {global_var_alt}")

def NOT_TRUE_demo_read_is_global_write_makes_local():
    '''
    Python sees that we might assign to size, and treats it as local, does not depend on actual write
    NB: the actual check of read before write is dynamic -- we have to call the function to provoke
     '''
    if 0:
        ## UnboundLocalError: local variable 'size' referenced before assignment
        print('prior write: size:', size, ' id:', id(size))
    if 0: size = 1024
    print('after write: size:', size, ' id:', id(size))
if 0: NOT_TRUE_demo_read_is_global_write_makes_local()

def demo_local_read_before_write_is_bogus():
    try:
        print('prior here_i_am:', here_i_am)
    except Exception as e:
        print('*** exception encountered ***', e)
    finally:
        return None

    if 0: here_i_am = 17
    print('after here_i_am:', here_i_am)
if 0: demo_local_read_before_write_is_bogus()

def silly_me(bigger_than_a_bread_box = size):
    size  = bigger_than_a_bread_box;
    print("size =", size)


##[]##
