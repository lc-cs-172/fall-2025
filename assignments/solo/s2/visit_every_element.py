print();                        # ensure a newline after the >>> prompt

print("================");
print("================");
print("================");

## demo min and max
small = min(-7, 42)
large = max(-7, 42)
average = (-7 + 42 + 0 + 3)/4

## demo assert
assert small == -7
assert large == 42
assert average == 9.5

## demo print
print("min(7,42) =", small)
print("max(7,42) =", large)
print("avg(7,42) =", average)

## define the list of data
data = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3]

## there are a whole lot of pieces here -- we'll discuss them in class
print("demo fancy printing: ", end='')
for i in range(len(data)):
    print(data[i], end='')
    if 0 == i: print('.', end='');
print();

##  ================================================================

## Assignment #2: compute values of data_min, data_max, and data_avg, and run this program.

## FYI: we define these values so this scaffolding will execute cleanly
data_min = None
data_max = None
data_avg = None

print("================")
print("and my answer is")
print("================")

print("min(data) =", data_min)
print("max(data) =", data_max)
print("avg(data) =", data_avg)

#[]#    
