a = 0
b = 0
c = 7
p = lambda x: a*x**2 + b*x + c

def tellme():
    print(f'{a=} {b=} {c=}')

def showme():
    tellme()
    xs = [ 0, 1, 2, 3]
    for x in xs:
        print(f'{x=} {p(x)=}')




[]
