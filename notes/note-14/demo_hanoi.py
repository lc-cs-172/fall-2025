## revised example from Pythonorama -- better names, make it DRY

def tiny_hanoi_move(source, target):
    print(str(source) + ' -> ' + str(target))

def tiny_hanoi_solve(source, spare, target, n):
    if n == 1:
        tiny_hanoi_move(source, target)
    else:
        tiny_hanoi_solve(source, target, spare, n - 1)
        tiny_hanoi_move(source, target)
        tiny_hanoi_solve(spare, source, target, n - 1)

##----------------------------------------------------------------
## build a better illustration ##
##----------------------------------------------------------------

## NB: using Python "trick" --
##     we do not *assign* to peg itself within functions, so we can access and manipulate this shared global
peg = [] # holds our 3 towers -- will hold a list of lists -- create global shared list we can manipulate below

def hanoi_show():
    for tower in peg:
        print(tower)
    print()

def hanoi_move(source, target):
        disk = peg[source].pop()
        peg[target].append(disk)
        hanoi_show()
    
def hanoi_solve(source, spare, target, n):
    """move top n items from source to target, using spare"""
    if n == 1:
        hanoi_move(source, target)
    else:
        hanoi_solve(source, target, spare, n-1)
        hanoi_move(source, target)
        hanoi_solve(spare, source, target, n-1)

def hanoi_run(size):
    """setup and solve Towers of Hanoi puzzle, moving size disks from peg 0 to peg 2"""

    print(f'\n==== Towers of Hanoi for {size} disks ====\n');

    ## initialize our configuration
    ##
    ## clear any prior configuration
    peg.clear()
    ## create peg[0], loaded with our disks
    peg.append([i for i in range(1,size+1)])
    ## create empty peg[1] and peg[2]
    peg.append([])
    peg.append([])

    hanoi_show()
    hanoi_solve(0, 1, 2, size)

def hanoi_demo():
    hanoi_run(3)
    hanoi_run(4)

hanoi_demo()

#[]#        
