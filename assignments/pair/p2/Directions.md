# Assignment #9: Binary Search Trees

This assignment is designed to continue with pair programming, focus on object
oriented programming, unit testing, and a beautiful data structure, the binary
search tree (a foundation for many wonderful algorithms).

## Submission Details

Each assignment has two or more authors, one primary submission, and secondary
submissions. Yes, multiple submissions, one each (to satisfy Google Classroom
logistics).  The write-up is a single ASCII .txt file called `bst_write-up.txt`.
Each write-up contains *brief* entries which

* identify your programming partners
* indicate the primary and secondary submitters
* state how you used AI if at all
* mention how you shared responsibilities
* using a format akin to Pascal's Triangle, where the parent is centered above
  the children, provide 2 examples of a BST layout with 7 keys in range(1,8),
  showing
  - maximum depth
  - minimum depth
* describe what you learned

The secondary submitters should be able to just submit the common write-up file.

You'll each get the same homework score based on the primary submission.

## Logistics

Create two Python files, `bst.py` and `bst_test.py`.

In bst.py, use Python OOP to define BST classes `Tree` and `_Node`.
The Tree needs to support

|routine						| purpose									|
|----							|----										|
| insert(self, key, val)		| duplicate keys NOT allowed				|
| lookup(self, key) -> (k,v)	| returns None if no such key				|
| verify(self) -> bool			| verifies the integrity of the tree		|
| visit(self, visitor)			| in-order visitor(key, val) for every item	|
| `__init__`					| usual										|
| `__repr__`					| usual										|
| `__str__`						| usual										|
| `__len__`						| more magic								|
| `__iter__`					| lots more magic							|

In bst_test.py, create your unit tests called test_XYZ, where XYZ indicates what
you're testing.  Make sure you test every function, including the iterator and
the verifier, with edge cases like 0,1,2,3,7,8,9 elements.  Use pytest to run
your unit tests, putting the result in bst_test.txt.

Go to this assignment in [LC-CS-172-Fall-2025](https://classroom.google.com);
submit your files.

## Extra Credit

Determine the expected depth of a binary search tree with elements inserted in
random order.  You'll need to provide `bst_random_depth.py`, the code you used
to determine the answer, and `bst_random_depth.txt`, a write-up explaining how
you got that answer and why you think it's correct.

## Primary Submission Files

#### required

* `bst.py`
* `bst_test.py`
* `bst.test.txt`
* `bst_write-up.txt`

#### extra credit

* `bst_random_depth.py`
* `bst_random_depth.txt`

## Secondary Submission Files

* `bst_write-up.txt`

Do not forget to hit the submit button.

#### []
