# LC-CS-172 Topics for Wed 24-Sep-2025

## Administrivia

* please mark your attendance in Google Classroom for today

* reminder: this week's assignment is due Friday  
it is a
[Pythonorama pair programming](https://github.com/alainkaegi/pythonorama/blob/main/software_development/pair_programming.md)
assignment -- please *find a partner*
    
* reminder: midterm I is this coming Monday

  - in-class, closed-book, pen-and-paper  
    **bring a pencil or pen**

* we'll do review for midterm I this coming Friday --  bring your questions

  - we will do a short practice exam  
    **bring a pencil or pen**

## Quote of the Day

    [reference](https://www.goodreads.com/quotes/9248998-the-devil-is-in-the-detail-is-an-idiom-that)

### ``The devil is in the details.``

    -- common idiom --

### ``God is in the detail.``

    -- Ludwig Mies van der Rohe (1886-1969) --

###  ``Le bon Dieu est dans le detail.``

    -- Gustave Flaubert (1821-1880) --

## Post-it Note Protocol

We're doing in-class active feedback today  
-- grab a red and green Post-it Note --  
you know what to do (refer to note-02).

## Feedback

### want: study guide for midterm I

* see ../note-04/

beyond what's described there, we've also covered

* linear search and binary search
  [Pythonorama search](https://github.com/alainkaegi/pythonorama/blob/main/algorithms/search.md)
* three different sorts in detail
  - analyzed their run time behavior
    + in general -- e.g., O(n**2) 
    + in detail -- e.g., n*(n+1)/2
  - analyzed their storage requirements
* Python reference semantics (like pointers to objects)
* Python list and dict and tuple semantics [**TBD** show unpacking]
* shallow and deep copies [**TBD** show deep copy]
* list comprehension
* name scoping (globals vs. locals)

### want: more in-class coding

Yup, we're headed in that direction -- but it takes time to cover the
basics you need to know to learn Python and do the assignments.

### want: show the sorts without the baggage

I understood this for me to code up the different sorts outside of the
test harness.

But there are two issues there.

1. Your assignment is to code up those sorts and plug them into the harness  
   I've described those sorts in class multiple times;  
   I'll not provide working code for those sorts now  
   -- that's *your* assignment.

2. The guts of the test harness are "out of scope"  
   I needed to provide the `instrument` you can use to view the sort
   behaviors; it's not a `demo*.py` routine -- you are not responsible
   for what's there, so you can ignore it if you wish.

### want: relate Python to C (and C++ and Java)

I will if/as I can -- but Python is a *very* different language.

- typing and type safety -- static vs. dynamic
- polymorphism -- static compile time vs. dynamic runtime
- object-oriented -- inherent from the get-go vs. shoe-horned in
- compiled vs. interpreted
- memory management

## Lecture

* O(1) == fixed [arbitrary] **constant**
* in-place *implied* (to me) O(1) space
* problem size is n, the length of the list to sort
* assignment: sort list in-place using O(1) space  

## Let's Code!

Have at it -- homework assignment #4, aka pair/p1

## []
