# LC-CS-172 Topics for Wed 15-Oct-2025

## Today's Hot Topics

* merge sort revisited -- done recursively
* intro to **Object Oriented Programming**
* review
* feedback

## Administrivia

* please mark your attendance in Google Classroom for today

* 2 assignments (solo/s5 and solo/s6) are both due this Friday

* CS Colloquium this Friday  
  an application of computer science in the real world  
  **how to connect the dots in the plane -- literally**

    October 17, 2025, JR Howard 102, 3:00-4:00 PM  
    Octilinear Flight Lines -- Overview -- a fast 2D metric MST technique

* invoking pytest

  - you should be able to invoke pytest in a terminal via  
        `python3 run_pytest.py`  
    even if you can't find the pytest command

  - you can also run pytest easily from within VS code

  - I'll live-demo in class

  - additional details below

## Merge-sort -- an optimal stable sorting algorithm! (*revisited*)

> [!NOTE]
> Focus is on recursive nature of algorithm and time complexity.  
> We allow ourselves to use O(n) extra storage.

### method (updated from original note-16) *NEW AND IMPROVED* -- now  w/ natural recursive version; fixed typos

    [natural recursive version]

	def merge_sort(data):
		""" merge sort the data, leaving result in data; return None """
		size = len(data)
		if size < 2: return None # already sorted

		split = size//2
		run1 = data[:split]
		run2 = data[split:]

		merge_sort(run1)
		merge_sort(run2)

		result = merge_runs(run1, run2)

		## return the result in-place
		data[:] = result
		return None

    [original iterative version, clearly showing limited extra storage]

		if len(data) < 2: return None # already sorted
        populate incoming_segments with sorted pairs of incoming data
        while len(incoming_segments) > 1
            outgoing_segments = merge_each_pair_of_segments(incoming_segments)
            incoming_segments = outgoing_segments
		assert len(incoming_segments) == 1
		data[:] = incoming_segments[0]
		return None

#### Re: space

* Note that you need O(n) extra working space to merge two sorted segments,  
  and O(lg n) extra stack space to handle the recursion depth

#### See also

- [Pythonorama search](https://github.com/alainkaegi/pythonorama/blob/main/algorithms/search.md)

- Sedgewic, Wayne, and Dondero, *Introduction to Programming in Python*,
  [Section 4.2](https://introcs.cs.princeton.edu/python/42sort/)

## Review

* re: recursion: sometimes it's hitting the base case to stop recursion  
  -- othertimes, it's finding the pot of gold at the end of the rainbow (eight queens)

* let's review Python globals and locals, and how to declare globals

## Feedback

* It's OK to grab a photo of what I write on the board  
  -- I will try to make prettier pictures

* pair programming and collaboration is critical  
  -- if it's a pair assignment, you really need to find a partner

* I'm serious -- you really need to come see me twice during office hours  
  to get full credit for participation

* I'll try and do a quick review of what we talked about last time  
  -- today it was merge-sort and recursion

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
