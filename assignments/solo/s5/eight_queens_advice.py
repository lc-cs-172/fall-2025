"""Purpose: Provide [verbose] advice about how to structure solving the
eight queens problem, leaving out important details and optimizations.

Advice:

Write a helper routine "is_queen_safe(row,col)" to answer the question
"given the current partial board configuration, is it safe to put the
queen in this row and col?"

Define function "place_all_queens(row)" which finds all the safe places
to place a queen in that row, and every time it finds a safe place, it
calls itself to find the safe places for queens in following rows.

In more detail, visit each column in that row, and ask the question
is_queen_safe(row,col).  If it's safe, then go on to the next row.

Always go on to check all the other columns in that row -- maybe another
placement in that row also works.

"""

## Here's what the advice looks like in running Python code.

################################################################
## NB: This is teaching code -- it is very verbose.
##     I would not write code like this for production.
################################################################

size = 4                        # size of the chessboard -- start small if debugging
queen_in_col = [None] * size    # given the row number, it tells us which column has the queen
safe_placements = []            # keep track of all the safe placements, so we can print 'em and count 'em at the end

def is_queen_safe(row,col):
    """ return True if and only if it's safe to place the queen in this row and col """
    ## this is a dummy routine for now, and gives the wrong answer.
    ## It is here to get this overall outline to run -- you will need to fix
    ## this and check that all columns and diagonals are clear.
    return (row == col) # FIXME: say OK if on the diagonal

def place_all_queens(row):
    """place a queen in each safe place in this row, and then call ourselves to go to the remaining rows"""
    ## Big Idea: we know we can only have 1 queen in each row -- so we only place 1 queen in each row

    ## You need a way to stop the recursion -- we're done if we placed all the queens
    if row >= size:
        ## success!  all the rows above us have safe queens -- this is a winning configuration
        ## NB: we MUST make a copy!!! -- otherwise, we will reference the queen_in_col object that keeps changing
        safe_placements.append(queen_in_col.copy())
        return None
        ##NOTREACHED##

    ## try every possible column in this row
    for col in range(size):
        if is_queen_safe(row, col):
            queen_in_col[row] = col # place this queen here
            place_all_queens(row+1) # find all the other safe placements
            queen_in_col[row] = None; # the queen has left the column

    return None

def show_queens():
    """show where all the queens are currently placed -- useful for debuggging, if we need it"""
    ## to be implemented if needed
    pass

def solve_eight_queens():
    place_all_queens(0)
    print(safe_placements)      # FIXME: we need to print one safe configuration per line
    ## TODO: print out the summary line

##================================================================
##================================================================
##================================================================

## here's another way of looking at the problem by using an explicit
## 2-dimentional board, indexed by row and column, containing characters
## to represent the position of the queens.  It may be easier to
## conceptualize what's going on, rather than tracking placement
## information via 1-dimentional arrays like queen_in_col.

U = 'U'
Q = 'Q'
_ = '.'

## examples taken from Directions.md

bogus    = [None]*size
bogus[0] = [U,_,_,_]
bogus[1] = [_,_,Q,_]
bogus[2] = [U,_,_,_]
bogus[3] = [_,_,_,U]

valid    = [None]*size
valid[0] = [_,_,Q,_]
valid[1] = [Q,_,_,_]
valid[2] = [_,_,_,Q]
valid[3] = [_,Q,_,_]

def print_board(board):
    print();
    for row in board:
        print(*row,sep='|')
    print();

print_board(bogus)
print_board(valid)

##[]##    
