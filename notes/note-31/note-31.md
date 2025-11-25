# LC-CS-172 Lesson Plan for Wed 19-Nov-2025

## Today's Hot Topics

* enrichment, exams, and self-discovery
* iterators (revisit simple Python example)
* pair programming w/ BST 

## administrivia

* please mark your attendance in Google Classroom for today

* FYI: assignment #9 due today, Wed 19-Nov-2025
  - pair programming -- expect 30 min in-class today

* NB: I made one small change to the assignment, and corrected a mistake --
  lookup should return a tuple of (key,value) or None, not just the value or
  None.	 Otherwise, there's an ambiguity -- did lookup return None because there
  was no matching key, or is None the value associated with the key?

## enrichment, exams and assignments, self-discovery

* enrichment

  - We're not training Python language lawyers
  - We are teaching the why and how and use of computer science
  - We are teaching how to program computer science solutions
  - Python has lots of nooks and crannies
  - There are things you need to know exist without the gory details
  - If you know it exists, and you need it, you can look it up
  - For example, I am not going to teach or test on exotic details
    + generators
	+ closures

* exams and assignments

  - this is an introductory course
  - the focus is on acquiring the basics
    + concepts
	+ vocabulary
    + understanding
	+ ability
    + facility

  That's what the exams and assignments are designed to assess.

* the final exam and assignment

  - final exam is MON 12/15/25 1:00P-4:00P

  - *in-class, pen and paper, closed-book*
    + **open note**: *one* 4x6 index card

  - we will review the topics on the final on Wed 12/10/25

  - no class Fri 12/12/25 -- reading period

  - there is no addendum for the final

  - final assignment will be due by Fri 12/05/25  
    accepted for partial credit up to 1 week late

* self-discovery

  I am trying to not only *tell* you, but *show* you **how** things work and
  **why** things work -- so you don't have to take it on faith -- you can see it
  for yourself; and when you have related questions later, you can figure it out.

  I'm not trying to send a mixed message.  Yes, follow the recipe.

  But note that assignment #9 is designed to offer a great deal more freedom and
  flexibility than you're used to; it is designed for you to figure out what
  makes sense to you, what works for you.

  The quality of your code is still very important, but you should explore what
  *works*" for you.  You know enough.  The training wheels are off the bike.
  For example, I pointed out you don't need recursion to search in the tree --
  but if you want to use it -- go ahead.

  I said you shouldn't use recursion to search based on ingrained habits
  (recursion used to be expensive) -- compilers are better, machines are faster,
  human time is more expensive, and often, recursion is the natural choice.

  I need to practice what I preach.

  **Avoid premature optimization**

  **Measure before you optimize.**

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

  - [demo_visit_iter_dfs.py](demo_visit_iter_dfs.py)

### Success!  An easy way to return value from visitor

* use local storage and nested functions

	```
	def demo_visit_easy(tree):
		'KISS: explicitly accumulate the visits in our local storage'
		my_visit_have = []
		def my_visitor(item):
			my_visit_have.append(item)
		tree.visit(my_visitor)
		return my_visit_have
	```

### Depth First Search

### Python iterator gory details (enrichment)

* iterABLE

  - provides an iterATOR

* iterable and iterator as *class*

  * `__iter__`	(iterable)
  * `__next__`	(iterator)
  * `iter(iterable)` returns iterator

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

# `***--->>> yield in-class programming <<<---***`

## Pair Programming w/ BST

* work on CS-172 pair programming assignment #9

#### []
