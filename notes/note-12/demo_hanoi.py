def hanoi(start, spare, end, n):
    if n == 1:
        print(start + ' -> ' + end)
    else:
        hanoi(start, end, spare, n - 1)
        print(start + ' -> ' + end)
        hanoi(spare, start, end, n - 1)

##----------------------------------------------------------------

peg = []                        # our 3 pegs

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

    ## use Python "trick" -- we do not *assign* to peg, so we access and manipulate global
    peg.clear()
    peg.append([i for i in range(1,size+1)])
    peg.append([])
    peg.append([])
    hanoi_show()
    hanoi_solve(0, 1, 2, size)

def hanoi_demo():
    hanoi_run(3)
    hanoi_run(4)

hanoi_demo()

#[]#        
