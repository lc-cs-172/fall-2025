##  ================================================================
## Assignment Description
##
##  Implement the function generate_pascals_triangle by replacing the
##  placeholder body of the function with your CLEAN working code.
##  You may also add your own functions in the student code section,
##  and use any imports used in class work.
##
##  For an extra challenge, use list comprehension and even the zip()
##  function.
##
##  The output must be well formatted;
##  generate_pascals_triangle(5) output looks like this:
##
##                      1
##		    1       1
##		1	2	1
##	    1	    3       3	    1
##	1	4	6	4	1
##
##  NB: The formatting is a key part of this assignment.
##  
##  Use spaces, not tabs, to get the formatting right 
##  -- tab display is NOT reliable.
##
##  The output really needs to look like that shown, where the columns
##  are aligned vertically, and the number below is *between* the pair
##  of numbers above.  The entries are integers -- they need to be right
##  aligned within their column.  (I've added explicit _ to represent
##  blanks to preserve formatting.)
##  
##  ______________________1______________________
##  __________________1_______1__________________
##  ______________1_______2_______1______________
##  __________1_______3_______3_______1__________
##  ______1_______4_______6_______4_______1______
##  
##  I've used many spaces between the columns -- use what you will, but
##  make sure the output is less than 80 characters wide, and the
##  numbers remain distinct and don't run into each other.
##
##  The first line is 1.
##  To generate the next line > 1
##    start the line with "1"
##    sum each pair from the line above
##    end the line with "1"
##
##  Only replace code in the student code section;
##    leave the rest of the file intact.
##  For now, you're welcome to have _disabled_ debugging code, 
##    but do not produce extraneous output in what you submit.
##  ================================================================

## ensure new line after any >>> interactive prompt
print();

## mark start of execution
print("""
=========================
==== Start of Output ====
=========================
""")

##================================================================
##================================================================
## vvvv student code goes goes BELOW vvvv -- leave this line alone
##================================================================
##================================================================

def generate_pascals_triangle(size):
    """ generate properly formatted Pascal's Triangle of the given size; size is the number of rows """
    ## ***--->>> YOUR CODE GOES HERE  <<<---***
    ## replacing these comments and the following pass statement
    pass

##================================================================
##================================================================
## ^^^^ student code goes goes ABOVE ^^^^ -- leave this line alone
##================================================================
##================================================================

## exercise the function
for size in range(7,10):
    print(f"\n==== Pascal's Triangle of Size {size} ====\n\n")
    generate_pascals_triangle(size)

print('''
===============
==== [QED] ====
===============
''')

#[]#    
