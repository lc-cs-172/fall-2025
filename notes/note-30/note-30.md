# LC-CS-172 Lesson Plan for Mon 17-Nov-2025

## Today's Hot Topics

* follow the recipe ... please
* revised rules of thumb
* returning a value from a visitor
* one version of the truth
* iterators (simple Python example)
* why parent pointers in our BST
* pair programming w/ BST 

## administrivia

* please mark your attendance in Google Classroom for today

* FYI: assignment #9 due date *is pushed out* to Wed 19-Nov-2025
  - pair programming -- expect 30 min today, 30 on Wednesday

## follow the recipe ... please

Each assignment is designed with a purpose.

Please, observe, and follow, the requested/required submission criteria.

I see folks misundertanding or ignoring the clear guidance and stateed purpose
of the assignments.

If I ask you make an omlette, and you make a souffle -- sure, a souffle is
harder -- but that's not the point -- can you make a good omlette?  We need a
good substantial main course omlette -- not a fancy optional dessert course
souffle -- we need the main meal.

## rules of thumb (revised)

* cf. [demo_visitor_using_state.py](demo_visitor_using_state.py)

		## **CAUTION**
		##     __init__ is not needed *if* we let Python automatically
		##     ***APPEAR*** 
		##     to initialize our object attributes from the class attributes
		##     -- but there are quirks
		##     -- THAT'S NOT WHAT HAPPENS
		##	   -- Keep it Simple, Simon (KISS) aka Keep it Simple, Stupid ...
		##
		##  **KISS**
		##     Simple is good -- and here's our good simple rule of thumb:
		##     ================================================================
		##     always use __init__ to declare and initialize all object attributes
		##     ================================================================
		##     -- avoid quirks
		##     -- avoid surprises
		##     -- avoid mistakes

		def __init__(self):

        ## Define and initialize all our attributes.
        ##
        ## It's a really good idea to have all the object attributes
        ## defined in one place so we know what all of them are.
        ##
        ## ================================================================
        ## Good-Simple-Rule_of-thumb -- put *all* attributes in __init__
        ## ================================================================
        ##

## how to *return* info from a visitor

* global variables (UGH!)
* use objects (Yay!)
* use a closure (Ooh!)

[demo_visitor_using_state.py](demo_visitor_using_state.py)

## One Version of the Truth

* Dynamic_Mean: re-uses reset()
* BST Node search(): used for both lookup and insert

## iterators

### BIG IDEA: function w/ state to return next item

### simple Python example

* Consider our simple linked list
* Uses fascinating new Python feature -- **yield**
  - (`yield` took 10 years to be added to Python -- 1991 to 2001)

	```
    def __iter__(self):
        ## defined as a generator function
        here = self.head;
        while (here != None):
            yield here
            here = here.next
	```

  - [demo_linked_list_iter.py](demo_linked_list_iter.py)
  - [demo_linked_list_iter_test.py](demo_linked_list_iter_test.py)

## why parent pointers in our BST

* not strictly necessary, but I find it helps ... a lot ...
  - alternative is to track path from root w/ stable tree

* advantages
  - debugging -- can find all neighbors, and even the whole tree
  - can always find root with walk up, given one node 
  - simple iterators if not Python (`yield` took 10 years to add)
  - allows tree modifications during traversal 

# `***--->>> yield in-class programming <<<---***`

### Python iterator gory details (enrichment)

  - re: functions (aka routine, method)
    - wo/ state (pure)
	- w/ state  (better to use method on object, object holds state)
     
    - deterministic
    - non-deterministic ('random')

* uses **lazy** evaluation

  - saves space
  - may save time too

* iterABLE

  - provides an iterATOR

* iterable and iterator as *class*

  * `__iter__`	(iterable)
  * `__next__`	(iterator)
  * iter(iterable) returns iterator

* generator *function*

  - created when function itself includes `yield`

* list comprehension

  - syntax - NB: introducing *new* feature -- `if condition`

	`expression for item in ITERABLE if condition`
    
  - uses square bracket notation [...]

* generator expression

  - like list comprehension,  
    but elements one-at-a-time
  - uses paren notation (...)

* demo

  - [demo_iterator.py](demo_iterator.py)
  - TBD: [live-coding -- countdown iterator as object](demo_countdown_object.py)

## Pair Programming w/ BST

* work on CS-172 pair programming assignment #9

#### []
