##  ================================================================
## Assignment Description
##
## NB: Detailed description of eight queens problem in ./Directions.md.
##
##  Using recursion, implement the function solve_eight_queens by
##  replacing the placeholder body of that function with CLEAN working
##  code.  Add your own functions in the student code section.  You may
##  use any imports used in prior class work.
##
##  Only replace code in the student code section;
##    leave the rest of this file intact.
##  For now, you're welcome to have _disabled_ debugging code, 
##    but do not produce extraneous output in what you submit.
##
##  The program needs to emit each successful configuration, and the
##  total number of successful configurations, using the following
##  output format.
##
##    One line for each non-attacking configuration
##       [5, 3, 6, 0, 7, 1, 4, 2]
##    which indicates that row 0 has a queen at column 5, ...
##    
##    A summary line including
##       Recursions=R
##    and
##       Solutions=N
##    where R is the total number of recursive calls,
##    and N is the total number of safe configurations.
##  ================================================================

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

def solve_eight_queens():
    ## ***--->>> YOUR CODE GOES HERE  <<<---***
    ## replace the entire body of this routine with your code
    ##
    solution = [5, 3, 6, 0, 7, 1, 4, 2]
    solution_count = 1
    recursion_count = 0
    print(solution)
    print(f"Recursions={recursion_count} Solutions={solution_count}")

##================================================================
##================================================================
## ^^^^ student code goes goes ABOVE ^^^^ -- leave this line alone
##================================================================
##================================================================

solve_eight_queens()

print('''
===============
==== [QED] ====
===============
''')

#[]#    
