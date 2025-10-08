## Purpose: demo action-at-a-distance

print("""
===============================
==== show storage diagrams ====
===============================
""");

foo = [1,2,3]
bar = ['x', 'y', 'z']
baz = [foo, bar]

print(f'before: {baz=}')

foo[1] = 'action-at-a-distance'
print(f'after: {baz=}')

print("================ why is it like that?  ================")

print('''
===========================================
A reference refers to (points to) an object.
A variable is a named reference.

An object is composed of basic elements (e.g., int), and references.

A reference does not point to a reference,
    but a reference can point to an object with a reference.

Expressions produce an object.
A reference in an expression refers to the underlying object.
Assigning an object to a variable actually assigns a reference.

Collections contain references to objects.

Some objects are mutable.

----------------------------------------------------------------

Read this code, including the comments and asserts, for illustrations.

===========================================
''')

foo = 17                        # foo -> object X w/ value 17
bar = foo                       # bar -> object X w/ value 17
print(f'.... {foo=} {bar=} ....')
assert id(foo) == id(bar)
assert foo == 17
assert bar == 17

foo = -1                        # foo -> object Y w/ value -1
pass                            # bar -> object X w/ value 17
print(f'++++ {foo=} {bar=} ++++')
assert id(foo) != id(bar)
assert foo == -1
assert bar == 17

foo = [17]                      # foo -> object A w/ value [17]
bar = [foo]                     # bar -> object B w/ value [@A]
print(f'==== {foo=} {bar=} ====')
assert foo == [17]
assert bar == [[17]]

foo[0] = -1                     # no change in foo or bar references, but foo -> object A w/ value[-1]
pass                            # bar is unchanged (-> object B), but object B w/ value [@A] == [[-1]]
print(f'|||| {foo=} {bar=} ||||') 
assert foo == [-1]
assert bar == [[-1]]

##----------------------------------------------------------------

print("=" * 50);
print("demo that a collection hold references to objects, not the variable holding the reference")
print("capture foo's value (a reference), then change foo -- captured reference does not change")
foo = [0,1,2,3]
bar = ['x','y']
baz = [foo, bar]
print(f'%%%% {foo=} {bar=} {baz=} %%%%') 

latch = foo                     # grab reference to object foo points to
assert latch is foo             # these point to the same object
assert latch is baz[0]          # these point to the same object

foo = ["now here"]              # change what foo points to
print(f'%%%% {foo=} {bar=} {baz=}\n {latch=} %%%%')
assert foo == ['now here']
assert latch == [0,1,2,3]
assert bar == ['x', 'y']
assert baz == [[0,1,2,3],['x','y']]

assert not latch is foo         # these point to different objects
assert latch is baz[0]          # these point to the same object

print("but the underlying object can change, if mutable")
## NB: we are not changing the referece, we are changing the underlying mutable object
latch[:] = 'action','at','a','distance' # NB: we don't need tuple notation here -- go figure
print(f'%%%% {foo=} {bar=} {baz=}\n {latch=}%%%%')
assert foo == ['now here']
assert latch == ['action','at','a','distance']
assert bar == ['x', 'y']
assert baz == [ ['action','at','a','distance'], ['x','y'] ]

##[]##
