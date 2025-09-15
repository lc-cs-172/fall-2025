# LC-CS-172 Topics for Mon 15-Sep-2025

## Administrivia

* please mark your attendance in Google Classroom

## Grading Details -- don't sweat the small stuff

We usually assign 100 base points for each assignment and test, and will
weight each assignment and test as described in the syllabus to get your
raw final score.

For example, assignment #2 has 100 base points.  But solo assignments
only make up about 30 points of the raw final score.

If we have 6 solo assignments overall, each solo assignment is worth
about 5% of your grade, so if you get a 80/100 on assignment #2, you'll
end up with 4 out of points in your raw final score.

That is, the impact of losing 20 points on assignment #2 translates into
losing 1 point on the raw final score.  And losing 5 points on
assignment #2 impacts your raw final score by only (5/100) * 5 == 0.25
points.

Here's the take away -- don't get too worked up about a few points here
and there on assignments -- focus on the learning, not the grade.  I use
points to emphasize the importance of the point (pun intended) I'm
trying to make.

Note too that the raw final score is a key input but not your final
grade -- as mentioned in the syllabus, I may adjust it based on
circumstances.

## Post-it Note Protocol

We're doing it today -- grab a red and green Post-it Note -- you know
what to do (refer to note-02).

### feedback topics

* Lectures are too mathematical?  It's par for and part of the course.

## Google Classroom Submissions

(Revised, w/ corrections; adapted from version originally posted in our
Google Classroom on Fri 12-Sep-2025)

* Hooray!  We have a clean submission recipe that seems to work for
everyone.  Verified today with MacOS and Win11.  Both successful
submissions were using VS code, but you can do it all with an editor of
your choice and the command line.

### How to create two ASCII files

one with just the program (pgm.py), and
one with the program output (pgm.txt)

* To create pgm.py

    in the editor of your choice, save the program code as pgm.py

* To create pgm.txt

  either

  - in VS code: run the program with a Dedicated Terminal; click `File`
    -> `New Text File`; copy (right click or Ctrl+Shift+C) the program
    output in the TERMINAL window into the new text file; save the file
    as pgm.txt
	
  or

  - run "python3 pgm.py > pgm.txt" in a TERMINAL

  In general, we'll provide a Python template for the assignment with
  well marked placeholder code you replace with your code.  Leave the
  rest of the file intact when you run it.

cf. [Pythonorama command_line](https://github.com/alainkaegi/pythonorama/blob/main/development_tools/command_line.md)

Either way, you create those two files, and that's what you submit.

## Class Collateral including Required Readings

### English Semantics

I try to be clear in the class collateral, while being polite.  At
times, those goals are in conflict.  I would like to say, "Please do it
this way ..."  -- but that makes it sound optional.  If required, I need
to say "Do it this way ...", which may sound harsh.  But it's not
optional, and Clarity is a Virtue.

### Syllabus

The syllabus is continuously being refined -- I point out notable
changes, so you don't have to keep rereading it.

### Notes

As mentioned, I often put more topics in the notes for a given class
than we end up covering.  I revise the notes, and move what we didn't
cover out of the old note and into the new note (e.g., note-03 ->
note-04).

The notes directories also include demo programs -- especially if
mentioned in the notes, those programs are also required reading.

### Assignments

Hopefully, the assignments are clear, if a bit detailed and direct.  See
English Semantics subsection above.

## Testing

### Dates and Logistics

As mentioned in the syllabus, we'll have 2 midterms and 1 final.

The exams are *closed-book in-class pen-and-paper* exams.  
**No calculators, no phones, no computers, no notes.**

The midterms are 1 hour.  The final is 3 hours.

Exam dates

  Test|date
  ---|---
  midterm I	|Mon 29-Sep-2025 in-class (tentative)
  midterm II|Mon 27-Oct-2025 in-class (tentative)
  final		|Mon 15-Dec-2025	1:00P-4:00P

### Subject Matter

I'm teaching a course, not writing a textbook.  There will be items that
are not written down by me -- you should take *good notes*.  Really.
You should **take good notes**.  Writing it down helps.  A lot.

The following are all fair game to ask you about on tests.

* anything taught in class, especially if with emphasis; e.g.,

  - linear and binary search -- algorithm and costs
  - selection sort --  algorithm and costs
  - something notable about computer scientist Brian Kernighan
  - in Python, what's the difference between `17` and `'17'`?
  - complete the following phrase: "The purpose of programming is `____`"
  
* anything in the  *required reading*

  if it is availabe in notes/ (e.g., notes-nn/*{note*.md,demo*.py}),  
  or is a reference to Pythonorama, it is **required reading**

  you don't need to run the demo code -- questions come from the code
  itself

  e.g.,

  - what's the value of `round(math.log2(10**3))`?
  - how do you compute in Python the logarithm to base 10 of a value?
  - what's a good multi-word Pythonic name for a binary search routine?
  - what's a good multi-word Pythonic name for a running sum variable?
  - what's the difference between Pascal case and camel case?

* how to apply what was taught; e.g.,

  - in a job interview, what algorithm would you use to code a sort
    routine for 100 numbers, and why?
  - would you use the same sort routine for 1e6 numbers (why or why not)?

## Objects and References (review)

		vocabulary  | meaning/understanding
		------------|---------------------------------------------------
		Value		| a bunch of bits
		Type		| how to interpret and operate on a Value
		Object 		| Type and Value	
		Reference	| memory address pointing to an Object

## Python Dynamic Polymorphism (review)

* reference points to an object, any object

* value of reference can change  
  so type of object can change

## Basic Simple Sorts (review)

* selection sort

* insertion sort

* bubble sort

  bubble sort is an *anti-pattern* -- don't do it!

    An [anti-pattern](https://en.wikipedia.org/wiki/Anti-pattern) is a
    solution to a class of problem which may be commonly used but is
    likely to be ineffective or counterproductive.

## Python Naming

cf. [Pythonorama names](https://github.com/alainkaegi/pythonorama/blob/main/style/names.md)

## Python Expressions

* usual arithmetic and logical expressions

* basic sequences

## Python Statements

* pass
* assignment
* function call
* flow control

## Python Flow Control

cf. [Pythonorama loops](https://github.com/alainkaegi/pythonorama/blob/main/control_structures/loops.md)

* for
* while
* break
* continue

cf. [demo flow control](./demo_control_flow.py)

## A Bit about Computing Machinery

* hardware circuits
* hardware architecture
  - cpu: ALU and registers
  - memory
  - I/O (terminal+disk+network)
* firmware and microcode
* operating system (kernel+root+user)
* ecosystem
* compilers and linkers and loaders
* interpreters

## []
