## import module contents (e.g., List and Item) directly into our scope (our namespace)
from demo_linked_list import *

def emit_list(ll):
    item = ll.head
    while item:
        print(f'{item} -> ', end='')
        item = item.next
    print('None')

def demo_emit_list():
    ll = List()
    one = Item(1)
    two = Item(2)
    ll.append(one)
    ll.append(two)
    emit_list(ll)

def verify_iter(ll, want):
    have = [ item for item in iter(ll)]
    assert have == want

##----------------------------------------------------------------

def test_empty():
    ll = List()
    verify_iter(ll, [])

def test_add_drop():
    ll = List()
    emit_list(ll)
    verify_iter(ll, [])

    one = Item(1)
    two = Item(2)

    ll.prepend(one)
    emit_list(ll)
    verify_iter(ll, [one])

    item = ll.remove(None)                      # remove head
    assert item is one
    emit_list(ll)
    verify_iter(ll, [])

    ll.append(one)
    ll.append(two)
    emit_list(ll)
    verify_iter(ll, [one, two])
    item = ll.remove(one)
    assert item is two
    emit_list(ll)
    verify_iter(ll, [one])

    ll.insert(one, two)
    emit_list(ll)
    verify_iter(ll, [one, two])
    item = ll.remove(None)
    assert item is one
    assert ll.head is two
    assert ll.tail is two
    emit_list(ll)
    verify_iter(ll, [two])

##[]##
