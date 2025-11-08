# LC-CS-172 Topics for Fri 07-Nov-2025

## Today's Hot Topics

* typos!!
* citing sources
* iterators
* pair programming w/ BST

## Administrivia

* please mark your attendance in Google Classroom for today

* course withdraw date is today (Fri 07-Nov-2025, by 4 PM)

* CS colloquim today

## Typos!!

* it's `__repr__` as in representation,  
  not `__repl__` as in blundered dunder read/eval/print/loop

* bisect testcase was wrong -- mistakenly checked tolerance against true root,
  rather than deviation of polynomial value from 0 -- worked for our testcase,
  but wrong in general.

## Citing Sources

* I'm seeing some pretty fancy programming

        ```
		if p(mid) < 0:

        vs.

		if p(lo)*p(mid) < 0:
		```
* abs(val) vs. (hi-lo)/2

## Iterators

### Big Idea: function w/ state to return next item

  - function (routine, method)
    - wo/ state
	- w/ state
     
  - deterministic
  - non-deterministic ('random')

* **lazy** evaluation

* iterABLE

  - provides an iterATOR

* iterator as *class*

  * `__iter__`
  * `next`
  * iter(iterable) returns iterator

* generator *function*

  - created using `yield`

* list comprehension
  
  - syntax: expression for item in ITERABLE if condition
    - NB: *new* info -- if condition
  - uses square bracket notation [...]

* generator expression

  - like list comprehension,  
    but elements one-at-a-time
  - uses paren notation (...)

* demo

  - (demo_iterator.py)[demo_iterator.py]
  - (demo_linked_list.py)[demo_linked_list.py]
  - (demo_linked_list_test.py)[demo_linked_list_test.py]

## OOP in Python (revisit)

* `__init__`
* `__repr__` (not repl)
* `__str__`
* `__len__`
* `__iter__` (here we go)

* [Pythonorama OOP classes](https://github.com/alainkaegi/pythonorama/blob/main/oop/classes.md)
* [Pythonorama OOP methods](https://github.com/alainkaegi/pythonorama/blob/main/oop/methods.md)
* [Pythonorama OOP `__magic__`](https://github.com/alainkaegi/pythonorama/blob/main/oop/magic.md)

## Pair Programming w/ BST

* work on CS-172 pair programming assignment #9

#### []
