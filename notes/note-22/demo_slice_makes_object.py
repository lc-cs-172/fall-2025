"""
demo that Python's slicing operation creates a NEW OBJECT,
leading to unexpected outcomes if you're used to other languages.
"""

def update_in_place(data, bump):
    for i in range(len(data)):
        data[i] += bump

def demo_weird():
    size = 10
    data = [i for i in range(size)]
    lump = data[:]
    assert data is not lump, 'slice created a new object'
    assert data == lump

    update_in_place(data, 10)
    print('data + 10', data)

    split = size//2
    update_in_place(data[:split], 100)
    ## note how our side effect was lost since we re-sliced our data
    print('data[:split] + 100 -- NOT!!!', data[:split])

    half = data[:split]
    update_in_place(half, 1000)
    print('half + 1000', half)
    
    
def main():
    print('\n==== demo slice creates new object ====')
    demo_weird()

##[]##    
