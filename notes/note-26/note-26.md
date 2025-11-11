# LC-CS-172 Topics for Mon 10-Nov-2025

## Today's Hot Topics

* midterm-2b addendum
* citing references
* visitor pattern
* pair programming w/ BST
* --- we got this far ---
* iterators

## administrivia

* please mark your attendance in Google Classroom for today

* FYI: assignment #9 due date *is pushed out* to Mon 17-Nov-2025
  - you will get 90 more minutes in class for the pair programming this week
  - [we had 20 minutes today]

## midterm-2b addendum

* **optional** -- with limited upside

* take-home programming assignment

* ajar-book
  - use your development environment (Python3, VS code, PyCharm)
  - no web searches
  - no AI 

#### ==== *** No AI *** ====
#### ==== No web searches ====


* timed -- intended for max one hour
* due Tue 11-Nov-2025 by 11:59 *PM*
* due Wed 12-Nov-2025 by 11:59 *PM* by ***prior*** request

### `***--->>> do NOT open midterm_2b_addendum.py <<<---***`
### `***--->>> until you start the exam <<<---***`

## citing references

Really ... you need to do this.

**Academic Integrity** requires it.

It is *dishonest* to not cite your sources.

## clean code

###	```Document your code.```
### ```How can we know if the code is right unless we know what the code is supposed to do?```
###	```Document your code.  But not excessively.  All comments should add value.```

## visitor pattern

* visit method on collection
* visitor function to operate on each element
* examples
  - print values in order
  - find average of items
  - verify BST integrity

### why use objects

#### Issues w/ find-the-average visitor

* needs [global] storage
* needs many related functions
* names are disjoint, related by convention
* pollutes global namespace

#### Solution: Encapsulate -- Use an Object!

* avoid global storage (aka `state`) -- unique to each object
* functions all go together, stay together, consistent naming
* related names of storage and functions are all together
* avoids namespace pollution -- access names through object

# ***--->>> You Are Here <<<---***

We got this far today.

## iterators

### BIG IDEA: function w/ state to return next item

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

* iterator as *class*

  * `__iter__`
  * `__next__`
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
  - [demo_linked_list_iter.py](demo_linked_list_iter.py)
  - [demo_linked_list_iter_test.py](demo_linked_list_iter_test.py)

## Pair Programming w/ BST

* work on CS-172 pair programming assignment #9

#### []
