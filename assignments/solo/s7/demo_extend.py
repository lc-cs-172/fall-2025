print("""
==== demo extend need not be conditional ====
[[ and slice values can be way whacky ]]
""")

size = 6
even = [ i for i in range(0,11,2) ]
odd  = [ i for i in range(1,12,2) ]

data = []

data.extend(even)
print('data', data)

data.extend(odd)
print('data', data)

data.extend(even[size:])
print('data', data)

data.extend(even[2*size:])
print('data', data)

data.extend(even[2*size:3*size])
print('data', data)

play = [1,2,3,4,5,6]

print(play[0:5:2])
print(play[5::-2])
print(play[5:3])
print(play[5:3:-1])
print(play[5:-10:-1])
print(play[-9:-10:-1])

[]
