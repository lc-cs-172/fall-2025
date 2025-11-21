print("""
Purpose: demonstrate the recurring build by reference trap and how to avoid it
""")

def spring_trap(wrap):
    rank = [0,0,0]
    grid = [ wrap(rank) for _ in range(3) ]       
    print('before update:', grid)
    grid[1][1] = 7
    print('after update:', grid)

def demo_trap_catch():
    print("demo_trap_catch")
    spring_trap(lambda x: x)

def demo_trap_avoid():
    print("demo_trap_avoid")
    spring_trap(list)

def main():
    demo_trap_catch()
    demo_trap_avoid()

[]    
