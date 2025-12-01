# LC-CS-172 Lesson Plan for Mon 01-Dec-2025

## Today's Hot Topics

* please mark your attendance in Google Classroom for today
* *draft* final exam topics posted (may be revised)
  - [final exam topics](https://github.com/lc-cs-172/fall-2025/blob/main/exams-PUBLIC/final_topics.md)
* new material you need to know
  -  source code management
  -  iteration redux
  -  `with` and context managers
  -  Python exceptions
  -  sorting techniques

## source code management

### NB: not Software Configuration Management

* ancient
    - SCCS
	- RCS
* centralized
    - svn
* distributed
    - git
* best practice
    - branch-based development
* example
    - how I use it for CS-172

## iteration redux

  + common
    - enumerate(seq)
    - zip(seq1,seq2)
  + dict
	- d.items()
	- d.keys()
	- d.values()

[demo_iter_redux.py](demo_iter_redux.py)

## `with`
  - `context manager` is a distinguished term
  - yes, there's a Python protocol for that
  - usage

	```python
	with open('demo_graphics.py', 'r') as f:
		script_code = f.read()
	```

## Python exceptions

[demo_simple_exception.py](demo_simple_exception.py)

## sorting techniques

* lexicographic sort order
* fast multi-key sorting using single-key sorting
* linear sorting 

## work in-class on assignment #10

#### []
