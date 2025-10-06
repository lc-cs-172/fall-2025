
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def demo():
    print("\n==== [open] ====\n")
    for n in range(7,15,2):
        print(f'{n}! = {factorial(n)=:8d}')
    print("\n==== [shut] ====\n")

demo()

#[]#
