# LC-CS-172 Topics for Mon 13-Oct-2025

## Quotes of the day

### The best way to predict the future is to invent it.

-- Alan Kay --

### Those who cannot remember the past are condemned to repeat it.

-- George Santayana --

## Administrivia

* please mark your attendance in Google Classroom for today

* CS Colloquium this Friday  
  an application of computer science in the real world

    October 17, 2025, JR Howard 102, 3:00-4:00 PM  
    Octilinear Flight Lines -- Overview -- a fast 2D metric MST technique

#### Opportunity to improving your midterm-1 score
  
* I'll collect your midterm-1 addendum at the end of class

## Responding to feedback

* As you requested, I'll identify *extra credit* portions of assignments and tests.  
  Note that extra credit will focus on synthesis and creativity; per  
  [L&C's grading policy](https://docs.lclark.edu/undergraduate/policiesprocedures/grading/):

		A Outstanding work that goes beyond analysis of course material  
		  to synthesize concepts in a valid and/or novel or creative way.

		B Very good to excellent work that analyzes material explored in  
		  class and is a reasonable attempt to synthesize material.

## Why we need to test our work -- we are human

* I just wrote a stable sort checker, and found an-easy-to-fix problem in two sorts I wrote
  - I got the sort order right, but failed the stability criterion

* Programming often involves lots of moving pieces -- we are human --
  - it's hard for humans to hold more than about 7 (some claim 4) distinct thoughts at the same time
  - [Wikipedia: The Magical Number Seven](https://en.wikipedia.org/wiki/The_Magical_Number_Seven,_Plus_or_Minus_Two)
  - that's a key reason we need to do testing

* Since it's easier to find and fix problems in relative isolation,
  - unit testing is especially useful.

## Reminder: Academic Integrity and use of AI (from the syllabus)

* You need to cite all your sources.

* You may use AI as a resource.

* You may not cut-and-paste AI output and submit it as your own work.

* See also [L&C Academic Integrity Policy](https://docs.lclark.edu/undergraduate/policiesprocedures/academicintegrity/).

## Reminder: Submission criteria (from the syllabus)

* program line length  <= 120 characters
* write-up line length <=  80 characters

## Order statistics (Part 2)

* what are some common functions and their growth rate?
  - ...
  - logarithmic
  - linearithmic (log-linear)
  - exponential

  [demo](demo_curves.py)
  
* logs are constant multiples of each other  
  for example, $\log_b(x)= c * \log_2(x)$  
  NB: *optional enrichment* proof was in prior lecture notes

* Q/ what do we mean when we say cost(n) = O(n log n))?  
  A/ that cost(n) <= n log(n) **EVENTUALLY**

* **Constants Do Matter**!!

  [demo](demo_curves.py)

* required reading, concentrating on big-O $\text{O}$ and big-theta $\Theta$ notation

  [Pythonorama analysis](https://github.com/alainkaegi/pythonorama/blob/main/algorithms/analysis.md)

## Merge-sort -- an optimal stable sorting algorithm!

> [!NOTE]
> Focus is on recursive nature of algorithm and time complexity.  
> We allow ourselves to use O(n) extra storage.

#### method (updated after class w/ natural recursive version; fix typos)

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

    [original iterative version, showing limited extra storage]

		if len(data) < 2: return None # already sorted
        populate incoming_segments with sorted pairs of incoming data
        while len(incoming_segments) > 1
            outgoing_segments = merge_each_pair_of_segments(incoming_segments)
            incoming_segments = outgoing_segments
		assert len(incoming_segments) == 1
		data[:] = incoming_segments[0]
		return None

#### See also

- [Pythonorama search](https://github.com/alainkaegi/pythonorama/blob/main/algorithms/search.md)

- Sedgewic, Wayne, and Dondero, *Introduction to Programming in Python*,
  [Section 4.2](https://introcs.cs.princeton.edu/python/42sort/)

#### FYI: optimal -- best possible (*worst-case*) *asymptotic* performance of any comparision-based sort

* sketch of proof (*optional enrichment*)
  - need n! leaves in binary decision tree
  - use Stirling's Approximation to prove depth =~ $$n * \log_2(n)$$
    * $$\ln(n!) = n * \ln(n) - n + O(ln(n))$$
	* $$\log_2(n!) = n * \log_2(n) - n * \log_2(e) + O(\log_2(n))$$
    * [Wikipedia Stirling's Approximation](https://en.wikipedia.org/wiki/Stirling%27s_approximation)

NB: *optimal* depends on problem specification

  - can sort faster if you can do more than just compare

## Live-coding:

* make sure **`pytest`** is up and running w/ solo/s6
* work on any CS-172 assignment you want
* ask your classmates for help if you wish
* help your classmates if they ask

#### []
