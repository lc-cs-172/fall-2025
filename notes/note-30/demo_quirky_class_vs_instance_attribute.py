"""
Purpose: 

This is a 'biology experiement' where we played with Python
to determine what it does.

This is ENRICHMENT -- you are not expected to know this code.

This is primarily for my benefit, so I don't lead you astray.

"""

##================================================================
## NB: There was something about this block below as a string
##     which REALLY messed up indent-region in Emacs python-mode.
##================================================================

##  Wha??
##
##  Function objects work differently from class objects?
##      wrt/ when the variable becomes 'local'??
##
##  Is this what I am seeing?
##
##    - on class function, on assignment???
##    - on function object, on static analysis????
##
##  my head hurts ...

    ## NB: We know that Python interns [some? small?] integers.
    ##     We need to see when new objects get created.
    ##     Therefore, don't use small integers!!!

##----------------------------------------------------------------

print("""
==== kickoff ====
""")

def kickoff(msg):
    print("""
================
==== """ + msg + """ ====
================
""")

def emit(tag, item):
    print(tag, item, 'id:', id(item))

def note(msg):
    print('\n', msg)

##----------------------------------------------------------------

## Inspired by original test case from Tsibo

kickoff('demo_class_attr: demo that some objects SEEM to share just one attribute')

class Test:
    _count = 0

x0 = Test
x1 = Test

## Note how x and x1 both reference the same object, Test, of type `type`, not `Test`;
## so using x and x1 to access an attribute will access the class attribute.
##
assert type(x1) is type
assert x0 is x1

## here is an instance of Test -- so this object type is Test
y = Test()
assert type(y) is Test

## change just one, and see both change
assert x0._count == 0
assert x1._count == 0
x0._count += 1
assert x0._count == 1
assert x1._count == 1

## Q/ They share _count -- why?
## A/ xN._count refers to the class attribute, not the instance attribute, since x0 and x1 refer to the SAME object
assert x0._count is x1._count

##----------------------------------------------------------------

kickoff('class Simple: demo that instance objects can all SEEM to share one attribute with class')

class Simple:
    count = 1000

zed = Simple
emit('zed.count:', zed.count)

one = Simple()
emit('zed.count:', zed.count)
emit('one.count:', one.count)

print('zed.count += 1')
zed.count += 1
emit('zed.count:', zed.count)
emit('one.count:', one.count)

two = Simple();
emit('zed.count:', zed.count)
emit('one.count:', one.count)
emit('two.count:', two.count)
assert zed.count is one.count
assert zed.count is two.count

print('one.count = 1010')
one.count = 1010
emit('zed.count:', zed.count)
emit('one.count:', one.count)
emit('two.count:', two.count)
assert zed.count is not one.count
assert zed.count is     two.count

print('random = 1010')
## Q/ Is python interning these not so small integers???
## A/ YES!!!
random = 1010 
emit('one.count:', one.count)
emit('random:', random)

print('two.count = 1020')
two.count = 1020
emit('zed.count:', zed.count)
emit('one.count:', one.count)
emit('two.count:', two.count)
assert zed.count is not one.count
assert zed.count is not two.count

## Q/ They seemed to share "count" -- why?
## A/ [FALSE] They all [always] refer to the class attribute.
##    Because they never change that value within the methods (no self.count = ...),
##    count remains nonlocal and refers to the enclosing scope, which is the class.
##    !False! count does not always refer to the class attribute -- assignment changes things
## A/ [HYPOTHESIS]
##  + symbol lookup is established by (scope rules) -- instance then class
##  + symbol is only created on instance when it is assigned "within" instance scope
##  + until then, instance finds the symbol on the class

##----------------------------------------------------------------

kickoff('class Simple_Repair_Bogus: demo that objects SEEM to share one common attribute')

class Simple_Repair_Bogus:
    count = 1000
    def bump(self):
        ## UnboundLocalError: cannot access local variable 'count' where it is not associated with a value
        count += 1

print('zed = Simple_Repair_Bogus')
zed = Simple_Repair_Bogus
emit('zed.count:', zed.count)
assert zed.count == 1000

print('one = Simple_Repair_Bogus()')
one = Simple_Repair_Bogus()
emit('zed.count:', zed.count)
emit('one.count:', one.count)
assert zed.count == 1000
assert one.count == 1000

print('zed.count += 1')
zed.count += 1
emit('zed.count:', zed.count)
emit('one.count:', one.count)
assert zed.count == 1001
assert one.count == 1001

print('one.count = 1010')
one.count = 1010
emit('zed.count:', zed.count)
emit('one.count:', one.count)

two = Simple_Repair_Bogus();
emit('zed.count:', zed.count)
emit('one.count:', one.count)
emit('two.count:', two.count)
assert zed.count == 1001
assert one.count == 1010
assert two.count == 1001

if 0:
    print('one.bump()')
    one.bump()
    emit('zed.count:', zed.count)
    emit('one.count:', one.count)
    emit('two.count:', two.count)

## Q/ They share count at times -- why?
## A/ See earlier hypothesis
## NB: The bogus attempt to repair, bump(), refers to its own local variable, not the object attribute.
assert zed.count is not one.count
assert zed.count is     two.count

##----------------------------------------------------------------

kickoff('class Simple_Fixed_Twisted: demo that objects seem to share just one attribute')

class Simple_Fixed_Twisted:
    count = 1000
    def bump(self,lump):
        self.count += lump

zed = Simple_Fixed_Twisted
emit('zed.count:', zed.count)

note('one = Simple_Fixed_Twisted()')
one = Simple_Fixed_Twisted()
emit('zed.count:', zed.count)
emit('one.count:', one.count)

note('zed.count += 1')
zed.count += 1
emit('zed.count:', zed.count)
emit('one.count:', one.count)

note('two = Simple_Fixed_Twisted()');
two = Simple_Fixed_Twisted()
emit('zed.count:', zed.count)
emit('one.count:', one.count)
emit('two.count:', two.count)

note('one.bump(101)')
one.bump(101)
emit('zed.count:', zed.count)
emit('one.count:', one.count)
emit('two.count:', two.count)

note('one.bump(102)')
one.bump(102)
emit('zed.count:', zed.count)
emit('one.count:', one.count)
emit('two.count:', two.count)

note('zed.count += 1')
zed.count += 1
emit('zed.count:', zed.count)
emit('one.count:', one.count)
emit('two.count:', two.count)

note('two.bump(2001)')
two.bump(2001)
emit('zed.count:', zed.count)
emit('one.count:', one.count)
emit('two.count:', two.count)

## Q/ They share count at times -- why?
## A/ See earlier hypothesis
assert zed.count is not one.count
assert zed.count is not two.count

##----------------------------------------------------------------

[]
