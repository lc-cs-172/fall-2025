# LC-CS-172 Topics for Wed 08-Oct-2025

## Administrivia

* please mark your attendance in Google Classroom for today

* Fall Break this week -- no homework due, no class on Fri 10-Oct-2025

* Homework -- you have *two* solo assignments, both due on Fri 17-Oct-2025
  - ../../assignments/solo/s5 -- eight-queens
  - ../../assignments/solo/s6 -- guided practice with recursion and pytest

## Opportunity to improving your midterm-1 score
  
#### on Monday (13-Oct-2025)
* you can turn in 
  - your original exam paper
  - a separate addendum on $8.5 x 11$ paper

* the addendum identifies
  - which question(s) you are revisiting
  - provides an *updated answer*
  - explains **why** it's a better answer

* you need to do more than just reproduce the markings on the exam  
  for example, you might explain
  - why the parens are important
  - why the quotes are important
  - the kind of expression (e.g., list comprehension)
  - how the expression gets evaluated (what it means)

* I'll review it for partial credit, and adjust your midterm grade as
  appropriate
 
## A Reminder about Grading

* From the syllabus
  - The grade of ***`B`*** reflects work that is normally done thoughtfully
	and thoroughly by students.  This is a good grade -- it's a
	fully-meets-expectations grade.
  - The grade of ***`A`*** is earned by students who consistently do
	outstanding work and who show an unusually strong commitment to
	being active participants in the learning process.
* This class policy is consistent with
  - [L&C's grading policy](https://docs.lclark.edu/undergraduate/policiesprocedures/grading/).
* Conclusion
  - If you do the minimum required, even if done very well, that's *not **`A`***
 	quality work, that's not 100/100.

## Recursion (continued)

* Fibonacci Sequence

  - [demo](demo_fibonacci.py)
  - need to memoize! (is_memoize=1)

## Order Statistics (Part 1)

* what does O(n**2) mean?
* why do we use O() analysis?
  - it is useful
  - it is practical
* how do we do O() analysis?
  - ignore lower order terms	(since highest order term always dominates)
  - treat non-zero constants as 1 (since n always gets big enough)

* what are some common functions and their growth rate?
  - constant
  - linear
  - quadratic
  - higher degree polynomials
  - logarithmic
  - linearithmic (log-linear)
  - exponential

* what is log(n)?
  - log(z)
  - log10(x)?
  - log2(t)?
  - ln(z)
  - lg(t)?

  [demo](demo_curves.py)
  
* logs are constant multiples of each other  
  for example, $\log_b(x)= c * \log_2(x)$  

  Don't just take my word for it, let's see why that's true.
  
  <!-- math in GFM markdown is a pain in the ass, -->
  <!--     as it differs from my local GFM support via pandoc -->
  <!-- on samson renders with MathML class="math T" -->
  <!--     w/ $: inline $$: display -->
  <!-- NB: the dollar signs have to be *tight* against the text!!! -->

	| 				|		|						|
	| ----			| :---:	| ----					|
	| $c$ 			| = 	| $\log_b(2)$  			|
	| $\log_2(x)$ 	| = 	| $y$  					|
	| $x$ 			| = 	| $2^y$  				|
	| $x$ 			| = 	| $(b^c)^y$  			|
	| $x$ 			| = 	| $b^{(c*y)}$  			|
	| $\log_b(x)$ 	| = 	| $c*y$  				|
	| $\log_b(x)$ 	| = 	| $c*\log_2(x)$  		|
	| $\log_b(x)$ 	| = 	| $\log_b(2)*\log_2(x)$	|
  
* Q/ what do we mean when we say cost(n) = O(n log n))?  
  A/ that cost(n) <= n log(n) **EVENTUALLY**

* **Constants Do Matter**!!

  [demo](demo_curves.py)

* required reading, concentrating on big-O $\text{O}$ and big-theta $\Theta$ notation

  [Pythonorama analysis](https://github.com/alainkaegi/pythonorama/blob/main/algorithms/analysis.md)

## Live-coding:

* make sure **`pytest`** is up and running w/ solo/s6
* work on any CS-172 assignment you want
* ask your classmates for help if you wish
* help your classmates if they ask

## []
