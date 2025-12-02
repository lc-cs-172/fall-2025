print("""
Purpose: Live-code a simple demo using the Python module `graphics`.
Example: Create a 3x3 tic-tac-toe board
ExtraCredit: animate the tic-tac-toe board
""");

def reload():
    """Emacs and Python on my Mac do not get along,
    so I use python3 -i to keep it simple.
    I edit the file in Emacs, then reload it back into Python.
    To reload, we 'source' this file via read() and exec() below.
    """ 
    with open('demo_graphics.py', 'r') as f:
        script_code = f.read()
    ## NB: must pass only globals to avoid populating this local vanishing scope
    exec(script_code, globals())

import graphics as g
import numpy as np                  # I really like using [r,c] to index
import time

SIZE = 3
OPEN = 0
NAUGHT = 1
CROSS = 2
DIMS = (SIZE,SIZE)
COLOR = [ 'grey', 'red', 'green' ]

class TicTacToe:

    def __init__(self):
        row = [OPEN] * SIZE 
        self.board = [ list(row) for _ in range(SIZE) ] # NB: we need to make each row independent, and avoid sharing
        self.win = None
        self.grid = None
        self.make_grid()

    def make_grid(self):
        "makes the graphics grid that we will display"
        self.win = g.GraphWin('Agent Location Grid', 400, 400)
        lo = -0.5
        hi = SIZE + 0.5
        ## conventional cartesian coordinate system, in which we appear to have rotated our board by 90 degrees
        self.win.setCoords(lo, lo, hi, hi)
        self.win.setBackground('light pink')

        self.grid = np.empty(DIMS, g.Rectangle)
        for row in range(SIZE):
            for col in range(SIZE):
                box = g.Rectangle(g.Point(row,col),g.Point(row+1,col+1))
                self.grid[row,col] = box
                marker = self.board[row][col]
                box.setFill(COLOR[marker])
                box.draw(self.win)

    def update_grid(self, row, col, agent):
        ## row is Y, col is X, so flip 'em, and adjust so row 0 is at the top
        box = self.grid[col, SIZE -1 -row]
        box.setFill(COLOR[agent])
        ##--box.draw(win)--## not allowed to draw it again ... yes, the color will auto-update ... 

    def emit_board(self):
        for row in self.board:
            print(row)

    def place(self, row, col, marker):
        assert self.board[row][col] == OPEN
        self.board[row][col] = marker
        if 1:
            print('DEBUG: row:', row, 'col: ', col, 'marker:', marker)
            self.emit_board()
        self.update_grid(row, col, marker)

def place(game, row, col, marker):
    game.place(row,col,marker)
    time.sleep(2)

def main():
    game = TicTacToe()
    game.emit_board()
    place(game, 1,1,NAUGHT)
    place(game, 0,0,CROSS)
    place(game, 0,1,NAUGHT)
    place(game, 1,2,CROSS)
    print("Hit Enter in the terminal to finish:", end='')
    ignore = input()

if __name__ == '__main__':
    main()
    ## NB: for some reason, Python 3.11 on RHEL 8 using Emacs and Python-mode complains
    ##        else:
    ##        ^^^^
    ##    SyntaxError: invalid syntax
    ##
    ##     but it works fine via python3 and reload() ... oh well ...
else:
    print("Enter main() in the terminal to draw the tic-tac-toe board.")

[]
