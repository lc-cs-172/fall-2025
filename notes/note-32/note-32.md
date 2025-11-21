# LC-CS-172 Lesson Plan for Fri 21-Nov-2025

## Today's Hot Topics

* Python recurring trap
* iterators as a baton pass
* assignment: simulate segregation w/ live-coding

## administrivia

* please mark your attendance in Google Classroom for today

* re: expected hours
  - 3 hr/wk class
  - 3 hr/wk study and homework
  - 2 wk assignment could take 6 or more hours
    programming, debugging, testing, documentation

## Python recurring trap

* Python builds by name (reference), not by value

  ```
  python
  rank = [0,0,0]
  grid = [rank] * 3
  print(grid)
  grid[1][1] = 7
  print(grid)
  ```

* [demo_python_trap_by_name.py](demo_python_trap_by_name.py)

## iterators

### could be a baton pass

* User -> Tree -> Node([subtree -> here -> subtree]) -> Tree -> User

    ```python
    class Tree:
		def __iter__(self):
			if self._root:
				for node in iter(self._root):
					yield node.key

    class Node:
		## simplified iterator using 'yield from' syntax
		def __iter__(self):
			if self.left: yield from iter(self.left)
			yield self
			if self.right: yield from iter(self.right)

    ```

### there is a lot of good teaching code here -- take a look

* [demo_visit_iter_dfs.py](demo_visit_iter_dfs.py)

## simulate segregation w/ live-coding

* [simulate segregation assignment](simulate_segregation_assignment.lnk)

* [demo_graphics.py](demo_graphics.py)

#### []
