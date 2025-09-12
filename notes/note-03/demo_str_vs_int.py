print("\nAnd we're off and running ...")

foo = "17"
bar = 17;

print(f"type(foo) = {type(foo)}")
print(f"type(bar) = {type(bar)}")

foo_int = int(foo);
bar_str = str(bar);

print(f"foo={foo} bar={bar}")
print(f"foo_int={foo_int} bar_str={bar_str}")

if foo == bar: print("BAD: have type mismatch")
if bar == foo: print("BAD: have type mismatch")

if foo != bar_str: print("BAD: what is going on?");
if bar != foo_int: print("BAD: what is going on?");

print("Game over.\nThanks for playing.");

#[]#

