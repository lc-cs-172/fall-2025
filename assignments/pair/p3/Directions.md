# Assignment #10: Simulate Segregation

This assignment is designed to continue with pair programming, object oriented
programming, unit testing, and extend into simple animated graphical displays.

## Overview

Implement Schelling's model of segregation, as described in [Frank McCown's
assignment](http://nifty.stanford.edu/2014/mccown-schelling-model-segregation/).

Your program should behave like the example embedded in the web page above.  Use
a smaller grid size but otherwise use the same default parameters
(similarity at 30%, red/blue ratio at 50%, and empty/total ratio at 10%).  At
the end of the simulation, print the number of rounds it took to get to
100% satisfaction.

At each step, you should first find all of the unsatisfied agents before any
moves and then move each unsatisfied agent one-by-one to a random unoccupied
cell.  Agents are allowed to move to cells that became vacant in the same round.

Clarification: an agent with no neighbors is satisfied.

You don't have to provide buttons or sliders, and you don't need to implement
the ability to stop or start -- when `main()` is called, jump right in: draw the
window, populate it, and start the simulation. Include the following line at the
bottom of the .py file:

    ```
    python
    if __name__ == '__main__': main();
    ```

Enable easy change of each parameter; place them all together in your program
near the top.

The parameters and their working values are

* HAPPY = 0.3             # fraction of neighbors if similar, agent is stable
* SPLIT = 0.5             # ratio of agents: type 1 vs. TOTAL
* USAGE = 0.9             # fraction of positions are occupied
* SIZE = 20               # edge size of the square grid
* PAUSE = 0.3             # delay in seconds between each simulation round
* AGENT_COLOR = [ 'grey', 'red', 'green' ] # color for cells: OPEN/ONE/TWO

You don't have to implement any variants, just the basic version.

Use small functions.  Use objects as appropriate.  In particular, the grid
should be an object with methods to create it, change it, and animate it.  Make
your code readable, using appropriate variable and function names to communicate
their purpose.  Verify every function and every object with a pytest-based test.

## Submission Details

Each assignment has two or more authors, one primary submission, and secondary
submissions. Yes, multiple submissions, one each (to satisfy Google Classroom
logistics).  The write-up is a single ASCII .txt file called
`simseg_write-up.txt`.  Each write-up contains *brief* entries which

* identify your programming partners
* indicate the primary and secondary submitters
* indicate the number of rounds required to stabilize
* state how you used AI if at all
* mention how you shared responsibilities
* describe the most difficult part of the assignment
* describe the best and worst aspects working as a team
* provide a rough estimate of hours outside of class to complete
  (team total, not each member; if it was 7+6+5, state 18)
* describe what you learned

The secondary submitters should be able to just submit the common write-up file.

You'll each get the same homework score based on the primary submission.

## Logistics

Create two Python files, `simseg.py` and `simseg_test.py`.

Use the Python module, `graphics`.
You may need to install it

        python3 -m pip install graphics.py

See also the small demo here (that we live coded in class)
[demo_graphics.py ](demo_graphics.py)

In simseg_test.py, create your unit tests called test_XYZ, where XYZ indicates
what you're testing.  Make sure you test every function.  Use pytest to run your
unit tests, putting the result in simseg_test.txt.

Go to this assignment in [LC-CS-172-Fall-2025](https://classroom.google.com);
submit your files.

## Extra Credit

* provide at least 5 different ways of initializing (*seeding*) the grid, and
  submit .png files of those initial configurations; configurations must include
  0. random (this is also part of the basic submission)
  1. checkerboard
  2. random occupied vs. open areas ('urban vs. rural')
  3. random *common* clumps of size k
     you choose one k, with 5 <= k <= 9
  4. you choose some other initial configuration method

  The bonus_write-up.txt includes the number of rounds each initial
  configuration took to stabilize.

## Primary Submission Files

#### required

* `simseg.py`
* `simseg_test.py`.
* `simseg_write-up.txt`

#### extra credit

* `bonus_seed.py`
* `bonus_seed_N.png`
* `bonus_write-up.txt`

## Secondary Submission Files

* `simseg_write-up.txt`

Do not forget to hit the submit button.

#### []
