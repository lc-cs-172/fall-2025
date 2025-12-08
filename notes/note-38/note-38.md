# LC-CS-172 Lesson Plan for Mon 08-Dec-2025

## Today's Hot Topics

* in-class student evaluations
* recurrence relations review
* problem hardness overview

## administrivia

* please mark your attendance in Google Classroom for today
* Today ... our penultimate class lecture -- feedback and fun stuff!
* [exam topics](final_topics.lnk) are finalized 
* Wed:	*last day of class* -- exam topics review
* Fri: 	No Class -- Reading Period  
  - NB: last chance to turn in assignments: Fri 11:59 PM
* Mon: 	Final Exam 1-4 PM, Olin 305
  * pen-and-paper in-person sit-down final
  * single 4x6 index card with personal notes
  * no computers, no smart devices, no calculators
  - 20 questions, 5 points each
  -  1 extra credit worth 10 points

## Recurrence Relations

* Let $T(1) = 1$

`familiar situation` 	| `recurrence equation` | `order statistic`
----					|	----						|	----
direct index			|	$T(n) = 1$					|	$\Theta(1)$
binary search 			|  	$T(n) = 1 + T(n/2)$			|	$\Theta(\lg(n))$
linear search 			|  	$T(n) = 1 + T(n-1)$			|	$\Theta(n)$
merge sort	  			|  	$T(n) = n + 2*T(n/2)$ 		|	$\Theta(n * \lg(n))$
selection sort			|  	$T(n) = n + T(n-1)$			|	$\Theta(n^2)$
distinct n-bit numbers	|	$T(n) = 0 + 2 * T(n-1)$		|	$\Theta(2^n)$
permutations of n items	|	$T(n) = 0 + n * T(n-1)$		|	$\Theta(n^0.5(n/e)^n)$

[Pythonorama Analysis](https://github.com/alainkaegi/pythonorama/blob/main/algorithms/analysis.md)

## Problem Hardness -- It Depends

### sorting -- it depends

* $O(n^2)$
* $O(n*\lg(n))$
* $O(n)$

### Traveling Salesman Problem (TSP) -- it depends

* exact solution is HARD
  - in general case: yes
  - in specific case: maybe

* approximate solution can be easy
  - 2X if Euclidean is very easy
  - 3/2X if Euclidean is now well known (Christofides, 1976)
  - PTAS if Euclidean is now well known (Arora, 1996)

#### []
