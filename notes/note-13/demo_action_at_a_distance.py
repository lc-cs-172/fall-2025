## Purpose: demo action-at-a-distance

foo = [1,2,3]
bar = ['x', 'y', 'z']
baz = [foo, bar]

print("""
==============================
==== show storage diagram ====
==============================
""");
print(f'before: {baz=}')

foo[1] = 'action-at-a-distance'
print(f'after: {baz=}')

##[]##
