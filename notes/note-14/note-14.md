# LC-CS-172 Topics for Mon 06-Oct-2025

## Administrivia

* please mark your attendance in Google Classroom for today

* Fall Break this week -- no class on Fri 10-Oct-2025

* Homework -- you have *two* solo assignments, both due on Fri 17-Oct-2025
  - Assigned last Friday: ../../assignments/solo/s5 -- eight-queens
  - Assigned today : ../../assignments/solo/s6 -- guided practice with recursion and pytest

## AI gets it wrong

  - [do insertion sort and bubble sort need the same number of swaps?](AI_gets_it_wrong.png)

  - [everything is an object -- NOT](EverythingIsAnObject--Not.png)


## Lecture: action-at-a-distance (updated -- new and improved!)

* storage diagram for list holding references to other objects

  [demo](demo_action_at_a_distance.py)

## Midterm-1

* review today
  
* Can a value in a tuple be an array?  
  	[Pythonorama tuples Q9](https://github.com/alainkaegi/pythonorama/blob/main/data_structures/tuples.md)

* How would you get the last three characters of a string `s`?  
    [Pythonorama strings Q6](https://github.com/alainkaegi/pythonorama/blob/main/data_structures/strings.md)

* [ (k, math.ceil(math.log2(k))) for k in range(1, 101, 20) ]  
    [Pythonorama loops](https://github.com/alainkaegi/pythonorama/blob/main/control_structures/loops.md)

		range(start, stop, step) returns an iterable of integers from
        start up to (but not including) stop, advancing step at a
        time. For example, range(2, 10, 3) produces the numbers 2, 5,
        and 8.

* [score distribution](midterm-1-scores.png)

	scores=[14, 35, 37, 38, 42, 44, 48, 56, 61, 61, 63, 63, 63, 64, 73, 75, 80, 81, 82, 85, 89, 100, 100]

## pytest

* each unit test is a function named **`test_`**`aspect()`
* unit tests are written using `assert`
* unit tests go in a file named `moniker_`**`test.py`**
* tests are run with the pytest command

  - [Pythonorama pytest](https://github.com/alainkaegi/pythonorama/blob/main/development_tools/pytest.md)
  - [Pythonorama testing](https://github.com/alainkaegi/pythonorama/blob/main/software_development/testing.md)

## Live-coding: Recursion (continued)

* Towers of Hanoi (revisit)

  - [demo](demo_hanoi.py)

* Fibonacci Sequence

  - [demo](demo_fibonacci.py)

## []
