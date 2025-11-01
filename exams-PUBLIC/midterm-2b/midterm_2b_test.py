import os

is_select_answer = os.getenv('LC_CS_172_SELECT_ANSWER')

print(f'DEBUG: is_select_answer={is_select_answer}')

if is_select_answer:
    import _HIDDEN_midterm_2b as dut
else:
    import midterm_2b as dut

##----------------------------------------------------------------

def test_sample_bang_bang():
    spots = {4, 5, 6, 7}
    have = dut.sample_bang_bang(spots)
    want = [(4, 8), (5, 15), (6, 48), (7, 105)]
    assert have == want

##----------------------------------------------------------------

def test_bisect_accurate():
    p = lambda x: x*x - 25
    lo = 0
    hi = 11
    for tol in [10**(-d) for d in range(7,13) ]:
        z = dut.bisect(p, 0, 11, tol)
        err = abs(z-5)
        assert 0 < err and err < tol
    
##----------------------------------------------------------------

def test_linked_list_empty():
    linked_list = dut.List()

def linked_list_emit(linked_list):
    if 1:
        pass
    else:
        ## helpful for debugging, not helpful running clean pytest
        item = linked_list.head
        while item:
            print(f'{item} -> ', end='')
            item = item.next
        print('None')

def test_linked_list_add_drop_len():
    linked_list = dut.List()
    linked_list_emit(linked_list)
    assert len(linked_list) == 0

    one = dut.Item(1)
    two = dut.Item(2)
    linked_list.prepend(one)
    linked_list_emit(linked_list)
    assert len(linked_list) == 1

    item = linked_list.remove(None)
    assert item is one
    linked_list_emit(linked_list)
    assert len(linked_list) == 0

    linked_list.append(one)
    linked_list.append(two)
    linked_list_emit(linked_list)
    assert len(linked_list) == 2
    item = linked_list.remove(one)
    assert item is two
    linked_list_emit(linked_list)
    assert len(linked_list) == 1

    linked_list.insert(one, two)
    linked_list_emit(linked_list)
    assert len(linked_list) == 2
    item = linked_list.remove(None)
    assert item is one
    assert linked_list.tail is two
    linked_list_emit(linked_list)
    assert len(linked_list) == 1

##----------------------------------------------------------------

def test_big_theta():
    f = dut.f
    g = dut.g
    N = dut.big_theta_breakpoint
    assert type(N) == int
    assert N > 1
    for n in range(1,N+1):
        assert f(n) >= g(n)
        assert f(n) < f(n+1)
        assert g(n) < g(n+1)
    for n in range(N+1,N*3):
        assert f(n) < g(n)
        assert f(n) < f(n+1)
        assert g(n) < g(n+1)

##[]##
