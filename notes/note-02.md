# LC-CS-172 Topics for Wed 10-Sep-2025

# `The only way to learn a new programming language is by writing programs in it.`

### -- Dennis Ritchie --

## Feedback

I want feedback.  Really.

I want to know what's working -- and what's not working -- for you.

I plan to use

* Post-it Notes (ongoing, e.g., today)
* conversations (anytime)
* email (anytime)
* office hours (come see me)
* Google Classroom Questions or Google Forms (will be ongoing)

### You have an advocate in Nero!

If you don't want to talk to me, talk to her.
She has already given me some of your useful, actionable feedback.

I was already planning to do more work at the board, and not lecture off
what's displayed on the projector.

I'll try to avoid interesting but not sufficiently relevant asides.
It would help me to know what that is for you.  Was it

* who invented Unix?
* who invented UTF-8?
* who invented the language Go?
* who wrote the original Hello World program?
* providing references I didn't teach about, so I won't test on?
* infinite number of real numbers between two different real numbers?
* too many quotes, maxims, and aphorisms?

Let me know -- give me feedback ;-)

## Administrivia and Clarifications

* Reminder: sign in to Google Classroom and mark yourself
present.  Please do it now -- poll is only open until 11:11.

* Reminder: college add/drop period ends at 4 PM on Fri 12-Sep-2025.
Access is via WebAdvisor.

* Post-it Notes Protocol:

  - take one red and one green Post-it Note
  - hold up the red one if I go too fast
  - hold up the green one if I go too slow
  - write an anonymous remark (green good, red bad) on one or both
  - stick the marked up note on the door on your way out

* Python is not a prerequisite for this course; teaching it is an
essential part of the course curriculum.  For those of you who know
how to program in Python already, it's slow going -- sorry about that.
We'll be done with the Python basics pretty soon, and the material
should become more interesting for all of you.

* Assignment Grading

  It's been rocky -- there be dragons in Google Classroom/Drive/Docs.

  Some of what's been graded has floating feedback comments, might not
  seem to fit on the page, or may even be in a different same-named file
  that's hard to locate in Google Drive.

  Google Drive makes it hard to find earlier versions of a file in a
  classroom setting -- expect that we won't copy the file to make it
  editable (since it's hard to find the original).

  `Simplicity is a Virtue.` Going forward, we're using TEXT (not binary)
  format files with `.txt` suffixes, and both file comments and private
  comments for details.

  I've done most of the grading so far -- if issues, talk to me.
  Nero will be taking the helm starting today.

  Now that I'm calibrated, I know doing a detailed code review of
  submitted code is too time consuming.  Going forward, expect few
  comments on your code, let the grading be your guide; ask if you have
  questions.  I plan to discuss important coding issues anonymously in
  class.

* The syllabus has been updated and clarified, to wit

### Late Policy

Unless otherwise indicated, assignment will be accepted up to 1 week late, with
*progressive grade impact*.

days late	| submit| reduction in score
---			| ---	| ---
1 			| Mon	|	-10%
2			| Tue	|	-20%
3			| Wed	|	-30%
4			| Thu	|	-40%
5			| Fri	|	-50%
more than 5	| N/A	| no credit

Please realize that the assignments are due when they are due, even if our class
does not meet that day.  Delaying your submission also delays your learning and
delays timely feedback.

### Teacher Information (note office hours details)

If you want to see me *outside of class or drop-in office hours*, you need
to **make an appointment**.

	Instructor	| Joseph P. SKUDLAREK
	Email		| jskudlarek@lclark.edu
	Office hours|
				| location SQRC (JR Howard 134)
				| Mon 9:00-10:00 AM (drop in or schedule)
				| Fri 9:00-10:00 AM	(drop in or schedule)
				| Tue 4:00-5:00 PM 	scheduled on my calendar
				| and otherwise 	by calendar appointment (send me email)
    Usual Hours | https://calendar.app.google/39ke7XHGDEjKMiSz5

	TA			| Samphasnearyroth (Nero) Chua
	Email		| samphasnearyrothc@lclark.edu
	Office hours| 
				| location Olin 305
				| Tues+Wed 5:00-6:00 PM

### File formats and names for submission

In general, all the files you submit for assignments are text files, simple
ASCII text files -- not Word documents, not Visual Studio code project files,
just simple ASCII text files.  They must be in TEXT (not BINARY) format, and
have the suffix `.txt`.  Python programs will have names like
visit_every_element.py.txt and the program's output will go into files with
names like visit_every_element.out.txt.

[We hope this works; Google Classroom has quirks we're still working out.]

#### News Flash: Looks like you can **unsubmit** your assignment

before it has been returned to you -- to be discussed in class

## What does data look like? [Round 2]

* a few details on integers and floating point

        2**10 == 1024 =~ 10^3 == 1e3

        32-bit integer has 2**32 different values

			unsigned	[0,    +4e9]
			signed		[-2e9, +2e9]

		floating point (IEEE 754)

		------	--------- --------	----------------
		type	size	  sig dig	maxval
		------	--------- --------	----------------
		float 	32 bits    ~7		3.4 x 10**38
		double 	64 bits	  ~16		1.8 x 10**308	
		------	--------- --------	----------------

* Python specific info
  - char vs. byte
  - str vs. int
  - quotes: ", """, ', '''
  - "msg" * count
  - fun w/ integers 		-- arbitrary precision
  - fun w/ floating point 	-- double is standard, numpy supports both

## Objects and References

vocabulary  | definition
--- 		| ---
Type		| how to interpret of bunch of bits
Object 		| type and value	
Reference	| memory address pointing to an object

### example

pi_value = 3.1416

	[[storage layout]]

pi_digit = [3,1,4,1,6]

    [[storage layout]]

## A bit about computing machinery

* hardware circuits
* hardware architecture
  - cpu: ALU and registers
  - memory
  - I/O
* firmware and microcode
* operating system (aka kernel)
* ecosystem
* compilers and linkers and loaders
* interpreters

### Note: Introduction => convey basic ideas, stay out of the weeds

In this course, we're explaining how things work in general, and good
ways to think about them.  Sometimes, it's not the absolute truth.
There may be *confusing* subtleties and edge cases we don't mention.

For example (so you can see why we skip some subtleties in this course)

#### Real World

How to start the car

* In general

  put key in ignition and turn

* Exception

  - foot not on brake
  - push button ignition
  - dead battery
  - no fuel

#### Computing

* In general:

  -	an object is stored in memory 
  - a reference holds the address of an object

* Exception:

  - system *could* interpret address 0 as None
  - system *could* work with transient object only in registers

## Linear Search and binary search [Round 2]

OK, let's do some math and prove lookup time for uniformly random item.  
Define n, the number of items we have to inspect, as the size of the problem.

* Linear Search

  - BestCaseTime == 1
  - ExpectedTime == ((n*(n+1))/2)/n == (n+1)/2 =~ (n/2)
  - WorstCaseTime == n

* Binary Search

  Recall that **lg(n)** means log to base 2 of the value n.  
  For example, lg(1024) == lg(2**10) == 10.

  - WorstCaseTime == lg(n)

## Python Expressions

* usual arithmetic and logical expressions

* sequences (e.g., list etc. described later)

## Python Statements

* pass
* assignment
* function call
* control

## Python Control Structures

cf. [Pythonorama](https://github.com/alainkaegi/pythonorama/blob/main/control_structures/loops.md)

* for
* while
* break

## []
