""" Purpose: demo basic Python flow control statements """


print("""
=========================
==== Start of Output ====
=========================
""")

data = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3]
print("data =", data);


## demo for and break
def find_first(data, want):
    """ return the index of the 1st instance of want, or -1 if not found """
    result = -1
    for i in range(len(data)):
        if data[i] == want:
            result = i
            break
    return result

result = find_first(data, 7)
print(f"find_first(data, 7) = {result}")
result = find_first(data, -7)
print(f"find_first(data, -7) = {result}")
    

## demo fancy for loop
def sum_smaller(data, limit):
    """ return the sum of all numbers in data < limit """
    sum = 0
    for item in data:
        if item < limit: sum += item
    return sum

limit = 5
result = sum_smaller(data, limit);
print(f"sum_smaller(data, {limit}) = {result}")


## demo while and continue
def strange_sum(data, limit, goal):
    """ return the smallest sum >= goal of numbers < limit """
    i = -1                      # non-standard initialization
    sum = 0
    while(sum < goal):
        i += 1
        item = data[i]
        if item >= limit: continue # NB: `>=', not `>'
        sum += item
    return sum

limit = 5
goal = 16
result = strange_sum(data, limit, goal)
print(f"strange_sum(data, {limit}, {goal}) = {result}")


print('''
===============
==== [QED] ====
===============
''')

#[]#
