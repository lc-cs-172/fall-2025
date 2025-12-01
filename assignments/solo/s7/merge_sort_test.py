import numpy as np

from merge_sort import merge_sort as my_sort

def test_null():
    data = []
    want = []
    have = data.copy()
    my_sort(have)
    assert have == want
    
def test_solo():
    data = [0]
    want = [0]
    have = data.copy()
    my_sort(have)
    assert have == want
    
def test_pair():
    data = [2, 1]
    want = [1, 2]
    have = data.copy()
    my_sort(have)
    assert have == want
    
def test_trio():
    data = [30, 10, 20]
    want = [10, 20, 30]
    have = data.copy()
    my_sort(have)
    assert have == want
    
def test_quad():
    data = [17, 128, 42, 64]
    want = [17, 42, 64, 128]
    have = data.copy()
    my_sort(have)
    assert have == want
    
def test_one_way():
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3]
    want = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 8, 9, 9, 9]
    have = data.copy()
    my_sort(have)
    assert have == want
    
def test_or_another():
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4]
    want = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 8, 9, 9, 9]
    have = data.copy()
    my_sort(have)
    assert have == want
    
def test_dr_seuss():
    data = ['the', 'cat', 'in', 'the', 'hat']
    want = ['cat', 'hat', 'in', 'the', 'the']
    have = data.copy()
    my_sort(have)
    assert have == want
    
def test_tongue_twister():
    data = ['a', 'box', 'of', 'biscuits,', 'a', 'box', 'of', 'mixed', 'biscuits,', 'and', 'a', 'biscuit', 'mixer']
    want = ['a', 'a', 'a', 'and', 'biscuit', 'biscuits,', 'biscuits,', 'box', 'box', 'mixed', 'mixer', 'of', 'of']
    have = data.copy()
    my_sort(have)
    assert have == want
    
def test_seuss_triple():
    data = ['the', 'cat', 'in', 'the', 'hat', 'the', 'cat', 'in', 'the', 'hat', 'the', 'cat', 'in', 'the', 'hat']
    want = ['cat', 'cat', 'cat', 'hat', 'hat', 'hat', 'in', 'in', 'in', 'the', 'the', 'the', 'the', 'the', 'the']
    have = data.copy()
    my_sort(have)
    assert have == want
    
def test_important_math_constants():
    data = [3.14159, 2.71828, 1.41421, 1.61803]
    want = [1.41421, 1.61803, 2.71828, 3.14159]
    have = data.copy()
    my_sort(have)
    assert have == want
    
def test_best_sorted():
    data = [0, 1, 2, 3, 4, 5, 6, 7]
    want = [0, 1, 2, 3, 4, 5, 6, 7]
    have = data.copy()
    my_sort(have)
    assert have == want

def test_anti_sorted():
    data = [7, 6, 5, 4, 3, 2, 1, 0]
    want = [0, 1, 2, 3, 4, 5, 6, 7]
    have = data.copy()
    my_sort(have)
    assert have == want

def test_big_boy():
    hand = np.random.randint(0,2**20,int(5e3))
    data = list(hand)
    want = data.copy()
    want.sort()
    have = data.copy()
    my_sort(have)
    assert have == want

##[]##    
