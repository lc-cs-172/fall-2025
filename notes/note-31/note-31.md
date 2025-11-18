# LC-CS-172 Lesson Plan for Wed 19-Nov-2025

## Today's Hot Topics

* iterators (revisit simple Python example)
* pair programming w/ BST 

## administrivia

* please mark your attendance in Google Classroom for today

* FYI: assignment #9 due today, Wed 19-Nov-2025
  - pair programming -- expect 30 min in-class today

## iterators

### BIG IDEA: function w/ state to return next item

### simple Python example

* Consider our simple linked list
* Uses fascinating new Python feature -- **yield**

	```
    def __iter__(self):
        ## defined as a generator function
        here = self.head;
        while (here != None):
            yield here
            here = here.next
	```

### details about BST Tree/Node division of work

  - [demo_visit_iter.py](demo_visit_iter.py)

### Python iterator gory details (enrichment)

* iterABLE

  - provides an iterATOR

* iterable and iterator as *class*

  * `__iter__`	(iterable)
  * `__next__`	(iterator)
  * iter(iterable) returns iterator

* generator *function*

  - created when function itself includes `yield`

* list comprehension

	`expression for item in ITERABLE if condition`
    
  - uses square bracket notation [...]

* generator expression

  - like list comprehension,  
    but elements one-at-a-time
  - uses paren notation (...)

* demo

  - [demo_iterator.py](demo_iterator.py)
  - TBD: [live-coding -- countdown iterator as object](demo_countdown_object.py)

# `***--->>> yield in-class programming <<<---***`

## Pair Programming w/ BST

* work on CS-172 pair programming assignment #9

#### []
