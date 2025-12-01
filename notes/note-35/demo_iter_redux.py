print("""
==== KICK-OFF ====
""")

data = [ i*i for i in range(5) ]

def lede(msg):
    print('\n====', msg, '====')

lede("demo simple iteration")
for item in data:
    print(item)

lede("demo enumerate")
for pair in enumerate(data):
    print(pair)

lede("demo zip")
## flip is some gnarly Python -- enrichment only!
flip = lambda x : (y := x.copy()).reverse() or y
for item in zip(data, flip(data)):
    print(item)

##----------------------------------------------------------------

meal = { 'protein': 'turkey', 'veggie':'string beans', 'dessert': 'pie' }

lede("demo dict iteration [same as dict.keys]")
for item in meal:
    print(item)

lede("demo dict.keys()")
for item in meal.keys():
    print(item)

lede("demo dict.values()")
for item in meal.values():
    print(item)

lede("demo dict.items()")
for item in meal.items():
    print(item)

lede("demo enumerate(dict)")
for what in enumerate(meal):
    print(what)

[]
