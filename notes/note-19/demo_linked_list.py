is_paranoid = True

class Item:
    """ super simple minimal linked list element """

    data = None                 # reference to our value payload
    next = None                 # referense to next item in the linked list, None if none

    def __init__(self, data):
        self.data = data
        # verify self.next auto-initialized to None
        assert self.next is None

    def __repr__(self):
        return f'.Item({self.data})'

class List:
    """ manages this list -- an Item is just an Item -- we make 'em into a linked list """

    head = None
    tail = None

    def __init__(self):
        if is_paranoid: self.verify()

    def __repr__(self):
        return f'.List(); list.head: {self.head} list.tail: {self.tail}'

    def insert(self, prior, item):
        """insert item after prior -- if prior is None, prepend at the head -- adjust list head and tail; return item"""

        assert item.next is None # no next when not yet in a list

        if self.head is None:
            assert (prior is None), "must insert as head in empty list"
            self.head = item
            self.tail = item
            item.next = None
        else:
            ## list is not empty, we can insert anywhere
            if prior is None:
                ## update the head
                item.next = self.head
                self.head = item
            else:
                ## splice item into list
                follow = prior.next
                prior.next = item
                item.next = follow
                ## update the tail if we're adding to the end
                if self.tail is prior:
                    self.tail = item

        if is_paranoid: self.verify()
        return item

    def remove(self, prior):
        """remove item after prior; return item removed"""
        if prior is None:
            ## remove the head
            item = self.head
            assert item, "have an item to remove"
            self.head = item.next
        else:
            item = prior.next
            assert item, "have an item to remove"
            prior.next = item.next

        if self.tail is item:
            assert self.tail.next is None, "last time has no next item"
            self.tail = prior

        item.next = None    # make Item well formed -- if not in the list, next is None
        if is_paranoid: self.verify()
        return item

    def prepend(self, item):
        return self.insert(None, item)

    def append(self, item):
        return self.insert(self.tail, item)

    def verify(self):
        """verify that list is well formed"""
        if self.head is None:
            assert self.tail is None
        else:
            assert self.tail is not None
            assert self.tail.next is None

            ## walk the list, ensure tail matches
            here = self.head
            while here.next:
                here = here.next
            assert here is self.tail

        return None

##[]##
