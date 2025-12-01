print("""
==== KICK-OFF ====
""")

data = [ i*i for i in range(3,8,2) ]
data.append('Fin')
size = len(data)

def lede(msg):
    print('\n====', msg, '====')

def drain(count):
    print(f"\n-- drain({count}) starting ...")
    spigot = iter(data)
    for k in range(count):
        item = next(spigot)
        print(item)
    print(f"... finished drain({count}) --\n")


lede("show me the data")
print('data', data)


lede("demo our simple drain routine")
drain(size-1)
drain(size)


lede("show how a simple exception works")
try:
    drain(size+1)
except StopIteration:
    print('Game Over, Thanks for Playing')


if 1:
    lede("demo try/finally")
    try:
        drain(size+1)
    finally:
        lede('finally fired, retains exception')


lede("NB: this *SHOULD* throw an uncaught exception")
drain(size+1)

[]        
