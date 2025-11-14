print("""
Modified from original test case from Tsibo 
""")

print("""
Wha??

And function objects work differently from class objects?
wrt/ when the variable becomes 'local'??

on class function, on assignment???
on function object, on static analysis????

my head hurts ...

"""

##----------------------------------------------------------------

print('class Test: demo that objects seems to share just one attribute')

class Test:
    _count = 0

x = Test
x1 = Test

x._count += 1
print(x1._count)

assert x._count == x1._count, "looks like they share -- why?"

##----------------------------------------------------------------

print('class Simple: demo that objects seems to share just one attribute')

class Simple:
    count = 1

zed = Simple
print('zed.count:', zed.count)

one = Simple()
print('zed.count:', zed.count)
print('one.count:', one.count)

print('zed.count += 1')
zed.count += 1
print('zed.count:', zed.count)
print('one.count:', one.count)

two = Simple();
print('zed.count:', zed.count)
print('one.count:', one.count)
print('two.count:', two.count)

##----------------------------------------------------------------

print('class Simple_Repair_Bogus: demo that objects seems to share just one attribute')

class Simple_Repair_Bogus:
    count = 1
    def bump(self):
        ## UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
        count += 1

zed = Simple_Repair_Bogus
print('zed.count:', zed.count)

one = Simple_Repair_Bogus()
print('zed.count:', zed.count)
print('one.count:', one.count)

print('zed.count += 1')
zed.count += 1
print('zed.count:', zed.count)
print('one.count:', one.count)

two = Simple_Repair_Bogus();
print('zed.count:', zed.count)
print('one.count:', one.count)
print('two.count:', two.count)

if 0:
    print('one.bump()')
    one.bump()
    print('zed.count:', zed.count)
    print('one.count:', one.count)
    print('two.count:', two.count)

##----------------------------------------------------------------

print('class Simple_Fixed_Twisted: demo that objects seems to share just one attribute')

class Simple_Fixed_Twisted:
    count = 1
    def bump(self):
        self.count += 1

zed = Simple_Fixed_Twisted
print('zed.count:', zed.count)

one = Simple_Fixed_Twisted()
print('zed.count:', zed.count)
print('one.count:', one.count)

print('zed.count += 1')
zed.count += 1
print('zed.count:', zed.count)
print('one.count:', one.count)

two = Simple_Fixed_Twisted();
print('zed.count:', zed.count)
print('one.count:', one.count)
print('two.count:', two.count)

print('one.bump()')
one.bump()
print('zed.count:', zed.count)
print('one.count:', one.count)
print('two.count:', two.count)

##----------------------------------------------------------------

[]
