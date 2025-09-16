##  ================================================================
## Assignment Description
##
##  Implement my_sort(), an *inplace* STABLE selection sort 
##  using only *basic* Python (e.g., simple loops)
##  by replacing the body of the my_sort function
##  with your CLEAN working code.
##
##  * put your code only there
##  * leave the rest of the file intact 
##  * do not use any Python sort() methods
##  * do not define your own functions
##  * do not import any Python modules or packages
##  * for now, you're welcome to add _disabled_ debugging code, 
##        but do not produce extraneous output in what you submit.
##
##  ================================================================

## ensure new line after any >>> interactive prompt
print();

## mark start of execution
print("================");
print("================");

def my_sort(data):
    ## ***--->>> YOUR CODE GOES HERE  <<<---***
    ## replacing these comments and the following pass statement
    pass

print("================")
print("exercise my_sort")
print("================")

data = []
print("\norigin:", data)
my_sort(data)
print("sorted:", data)

data = [0]
print("\norigin:", data)
my_sort(data)
print("sorted:", data)

data = [2,1]
print("\norigin:", data)
my_sort(data)
print("sorted:", data)

data = [30,10,20]
print("\norigin:", data)
my_sort(data)
print("sorted:", data)

data = [17,128,42,64]
print("\norigin:", data)
my_sort(data)
print("sorted:", data)

data = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3]
print("\norigin:", data)
my_sort(data)
print("sorted:", data)

data = ["the", "cat", "in", "the", "hat"]
print("\norigin:", data)
my_sort(data)
print("sorted:", data)

data = "a box of biscuits, a box of mixed biscuits, and a biscuit mixer".split()
print("\norigin:", data)
my_sort(data)
print("sorted:", data)

data = ["the", "cat", "in", "the", "hat"] * 3
print("\norigin:", data)
my_sort(data)
print("sorted:", data)

data = [3.14159, 2.71828, 1.41421, 1.61803]
print("\norigin:", data)
my_sort(data)
print("sorted:", data)

print("\n[QED]\n");

#[]#    
