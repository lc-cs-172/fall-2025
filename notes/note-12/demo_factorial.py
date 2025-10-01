def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def demo_factorial(n):
    print(f'{n}! = {factorial(n)}')

demo_factorial(7)

#[]#
