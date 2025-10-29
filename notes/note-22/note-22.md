# LC-CS-172 Topics for Wed 29-Oct-2025

## Today's Hot Topics

* lambda expressions
* binary search trees (BST)
* pair programming w/ BST

## Administrivia

* please mark your attendance in Google Classroom for today

* I'll return midterm-2 this coming Friday (in two days)
  - addendum due in class on Wed 05-Nov-2025

* midterm progress reports (green/yellow/red) went out on Tuesday
  - course withdraw date in 10 days (Fri 07-Nov-2025, by 4 PM)
  - will post current score early next week (before #2 addendum)

* new assignment today: pair programming with Binary Search Trees
  - NB: skipping  assignment doing merge_sort with linked lists

## Stacks/Queues/Deques (quick review)

* stack: aka push-down stack
  - single ended
  - push
  - pop
  - LIFO -- last-in, first-out
  - use: call-stack, expression evaluation
  
* queue: a kind of pipeline
  - double-ended
  - insert
  - remove
  - FIFO -- first-in, first-out
  - use: first come, first serve, maintain order

* deque: a stack on both ends
  - double-ended
  - push and pop on each end

## Surprising Python

* `data[slice]` is a whole new object

* [demo](demo_slice_makes_object.py)

## Lambda Expressions

```python
f = lambda x,y: x*y
print(f(2,3))
```

## Binary Search Trees

* Node
  - key
  - value
  - parent
  - left child
  - right child

* Tree
  - root node (could be None)
  - all nodes are ordered
  - supports lookup
  - supports ordered traversal


## OOP in Python

* __init__
* __repl__
* __str__
* __len__
* __iter__ (1st pass)

* [Pythonorama OOP classes](https://github.com/alainkaegi/pythonorama/blob/main/oop/classes.md)
* [Pythonorama OOP methods](https://github.com/alainkaegi/pythonorama/blob/main/oop/methods.md)
* [Pythonorama OOP __magic__](https://github.com/alainkaegi/pythonorama/blob/main/oop/magic.md)

## Live-coding

* work on any CS-172 assignment you want
* ask your classmates for help if you wish
* please help your classmates if they ask

#### []
