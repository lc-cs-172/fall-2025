# LC-CS-172 Topics for Mon 10-Nov-2025

## Today's Hot Topics

* midterm-2b addendum
* citing references
* iterators
* pair programming w/ BST

## administrivia

* please mark your attendance in Google Classroom for today

* FYI: assignment #9 due date is **not** pushed out  
  -- you will get 90 more minutes in class for the pair programming this week

## midterm-2b addendum

* take-home
* timed -- intended for max one hour
* ajar-book
  - development environment (Python3, VS code, PyCharm)
  - no web searches
  - no AI 

#### No AI!!!  No web searches!!!

### `***--->>> do NOT open midterm_2b_addendum.py until you start the exam <<<---***`

* due Tue 11-Nov-2025 by 11:59 *PM*
* due Wed 12-Nov-2025 by 11:59 *PM* by ***prior*** request

## citing references

Really ... you need to do this.  Academic integrity requires it.

## clean code

###	```Document your code.```
### ```How can we know if the code is right unless we know what the code is supposed to do?```
###	```Document your code.  But not excessively.  All comments should add value.```

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
