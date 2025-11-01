# CS-172 CS II Fall 2025

##  midterm #2b

* take home
* open book
* due Mon 03-Nov-2025 by 11:59 PM
* due Wed 05-Nov-2025 by 11:59 *AM* by prior request
  - e.g., sports, theatre, other pre-existing plans

## Scoring

		There are 4 problems.
		Each problem is worth 25 points.
		Extra good answers get 5 bonus points.
		You could theoretically score 120/100.
		
## Logistics

* modify `midterm_2b.py` to solve each problem.
* ensure `midterm_2b_test.py` passes using pytest
* store pytest output in `midterm_2b_test.txt`

### submit in Google Classroom

* required

  - `midterm_2b.py`
  - `midterm_2b_test.py`
  - `midterm_2b_test.txt`

* optional

  - `midterm_2b.png`

## Extra Credit

In all cases, extra credit can be award for exceptionally clean code: functions
are documented; variable names are natural and their purpose intuitive based on
their names; helpful but not excessive comments; and the the code is well
formatted -- form follows function.

## Problems

1.  `n!` is the notation for factorial.  `n!!` is the notation for double
    factorial.  You have code for `double_factorial` in `midterm_2b.py`.  Use it
    and list comprehension to implement the function `sample_bang_bang`.

1.  Using recursion, correctly implement the function `bisect` in `midterm_2b.py`.

1.  You have code for a complete linked list implementation in `midterm_2b.py`
    using `List` and `Item` classes.  Modify it to maintain the length (number of
    elements in the linked list) using O(1) overhead in speed and space.

    For full extra credit on this problem, make sure you update the `verify`
    function to check the length.

1.  $\Theta$ is big-theta. Every function $f(n) = \Theta(n*\log_2(n))$
    is always less than than              $g(n) = \Theta(n^2)$
    for all values of $n > N$ for some N.

	A function $f$ is strictly monotonically increasing if $f(y) > f(x)$ whenever
    $y > x$.  For example, $n*\log_2(n)$ and $n^2$ are both strictly
    monotonically increasing for $n\ge1$.

    For this problem, only consider integers $n > 0$.  Define strictly
    monotonically increasing functions $f(n) = \Theta(n*\log_2(n))$ and $g(n) =
    \Theta(n^2)$ and integer constant $N > 1$ such that $f(n) \ge g(n)$ for $n$
    in the closed interval $[1,N]$ and $f(n) < g(n)$ for all $n > N$.

    For full extra credit on this problem, graph the functions $f$ and $g$ in
	the interval $[1,2N]$ and submit the resulting `midterm-2b.png` file.

#### [Fin]
