# LC-CS-172 Topics for Fri 17-Oct-2025

## Quotes of the Day

### premature optimization

	  We should forget about small efficiencies, say about 97% of the time:  
		  **premature optimization is the root of all evil**.  
	  Yet we should not pass up our opportunities in that critical 3%.  
							-- Donald Ervin Knuth
  
###  Good enough is good enough.

	  Systems engineering is the art of the good enough.  
							-- Alexander Kossiakoff & William N. Sweet

	  A poem is never finished, only abandoned.  
							-- Paul Valéry, French critic & poet (1871--1945)

## Today's Hot Topics

* discuss eight_queens
* review merge_sort
* running reliable experiments
* intro to **Object Oriented Programming**

## Administrivia

* please mark your attendance in Google Classroom for today

* 2 assignments (solo/s5 and solo/s6) are both due **today**

* CS Colloquium today  

    October 17, 2025, JR Howard 102, 3:00-4:00 PM  
    Octilinear Flight Lines -- Overview -- a fast 2D metric MST technique

## Review

* merge-sort -- how many copies?

## Running experiments

* why do we need multiple runs?
  - consider flipping a fair coin 4 times -- what do you get?  
    ("4th" row of Pascal's Triangle!)

* why do we need long runs?
  - consider the fixed overhead mixed in with the varying runtime
  - see how it relates to order statistics!  
    [demo](demo_domination_eventually.py)

* law of diminishing returns

* extra credit re: Amdahl's Law
  - limits on absolute improvement

	"the overall performance improvement gained by optimizing a single part of a
    system is limited by the fraction of time that the improved part is actually
    used".

    [Wikipedia Amdahl's law](https://en.wikipedia.org/wiki/Amdahl%27s_law)

	![Amdahl's law illustration](AmdahlsLaw.svg)

	[Image credit: Daniels220 at English Wikipedia, CC BY-SA 3.0]	(https://commons.wikimedia.org/w/index.php?curid=6678551)

## Introduction to Object Oriented Programming in Python

OOP is a ***fundamental technique*** -- it is an essential tool in your programming toolbox.

### The Big Idea

* You can define your own **Type** of *Object*
  - You can define what it does
  - You can define how it does it
* You can create Objects of that Type
* OOP enables wonderful modularity
* OOP enables powerful abstraction/isolation
  - the interface says what the Type does
  - how it does it is up to the Type's implementation
* Objects can self-manage (think *modularity*)
* Objects can depend on other Objects
  - via inheritance (*is-a*)
  - via composition (*has-a*)
  - via interface (*like-a*)

* [Pythonorama OOP classes](https://github.com/alainkaegi/pythonorama/blob/main/oop/classes.md)
* [Pythonorama OOP methods](https://github.com/alainkaegi/pythonorama/blob/main/oop/methods.md)

## Live-coding

* make sure **`pytest`** is up and running w/ solo/s6
  - install: python3 -m pip install [--user] pytest
  - invoke:
    * pytest  
	-or-  
    * python3 run_pytest.py  
    -or-  
    * use VS code

	to set up pytest in VS code, visit any .py file and configure
	`testing` (click on the flask icon) to use pytest (*not* unittest)

    to run pytest, click on a little invoke icon (a triangle) at the top
	of the `testing` section in the left hand pane, or in the pytest
	file banner

* work on any CS-172 assignment you want
* ask your classmates for help if you wish
* please help your classmates if they ask

#### []
