a = [1,2,3]
b = a
print(f'{id(a)=} {id(b)=} {(a is b)=} {(a == b)=}')

b = [1,2,3]
print(f'{id(a)=} {id(b)=} {(a is b)=} {(a == b)=}')

##----------------------------------------------------------------

def alter_whole_name(x):
    print(f'prior {x=}')
    x = [ i for i in range(6) ]
    print(f'after {x=}')

def alter_one_item(x):
    print(f'prior {x=}')
    x[0] = "Fred and Ginger"
    print(f'after {x=}')

def alter_both_item_name(x):
    print(f'prior {x=}')
    x[0] = "Fred and Ginger"
    print(f'after whack item {x=}')
    x = [ "X marks the spot", "That is all" ]
    print(f'after whack name {x=}')

##----------------------------------------------------------------

_action = [
    alter_whole_name,
    alter_one_item,
    alter_both_item_name,
]

for action in _action:
    print('================')
    a = [ 1, 2, 3 ]
    print(f'{action} prior {a=}')
    action(a)
    print(f'{action} after {a=}')
    print('================')

##----------------------------------------------------------------

##[]##
