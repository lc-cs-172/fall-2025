print("""
==== demo ====
""")

"""
Purpose:

Super simple BST with only keys, without values or parents,
used to demo visitors and iterators.

Note how we have our "external" (Tree) API based on keys
and our "internal" (Node) API based on Node objects.

"""

##----------------------------------------------------------------

class Tree:
    def __init__(self):
        self._root = None

    def __repr__(self):
        ## NB: using the 'static' call syntax since self._root can be None
        return Node.__repr__(self._root)

    def __iter__(self):
        ## NB: Tricky! yielding items from an iterator which yields items
        ## and note how we hide internal nodes and expose external keys
        if self._root:
            for node in iter(self._root):
                yield node.key

    def visit(self, visitor):
        self._root.walk(visitor)

##----------------------------------------------------------------

class Node:
    "Node is an internal class, expose the guts -- attributes are public inside"

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        if not self:    return "Null"
        else:           return str(self.key)

    def __repr__(self):
        if self:
            return (
                "Node:"
                + " here: " + str(self.key)
                + " left: " + Node.__str__(self.left)
                + " right: " + Node.__str__(self.right)
            )
        else:
            return "Null"

    def __iter__(self):
        if self.left:
            for node in iter(self.left):
                yield node
        yield self
        if self.right:
            for node in iter(self.right):
                yield node

    def walk(self, visitor):
        if self.left: self.left.walk(visitor)
        visitor(self.key)
        if self.right: self.right.walk(visitor)

##----------------------------------------------------------------
##----------------------------------------------------------------

## Use global storage to accumulate visitor related updates

visit_have = None

def visit_setup():
    'get ready for the next visit'
    global visit_have
    visit_have = []

def visit_visitor(item):
    'track what we see'
    visit_have.append(item)

def demo_visit(tree):
    'demo how this works; we implicitly accumulate the visits in our global storage'
    'NB: we DO NOT control the flow of execution -- visit chooses when to call our visitor'
    visit_setup()
    tree.visit(visit_visitor)

##----------------------------------------------------------------

def demo_iter(tree):
    'demo how we can use an iterator to visit each item when we want to'
    'NB: we control the flow of execution -- we call the iterator when we want another'
    result = []
    for key in iter(tree):
        result.append(key)
    return result

##----------------------------------------------------------------

def build_subtree(lo,hi):
    "return balanced subtree build from integers [lo,hi)"
    """
    KISS: This is test code -- with restricted usage --
    we 'know' we are building a full BST,
    so we just cleanly cut in half each time;
    and yes, we assert this pre-condition -- easy to do, important to do
    """
    if 1 == hi-lo:
        return Node(lo)
    mid = (lo+hi)//2
    assert mid-lo == hi-1-mid    # ensure we cut the interval perfectly
    root = Node(mid)
    root.left = build_subtree(lo,mid)
    ## I am not a huge Python fan ... I had a typo, "rigth", w/ silent failure
    root.right = build_subtree(mid+1,hi)
    if 1: print(f'DEBUG: built subtree {root}')
    return root

##----------------------------------------------------------------

tree = None     # make it a global, so it's easy to inspect interactively

def main():
    global tree
    lo = 1
    hi = 8
    tree = Tree()                               # empty tree
    tree._root = build_subtree(lo,hi)           # testing code -- stuff in tree
    tree_have = [ i for i in range(lo,hi) ]     # what we put in the tree

    demo_visit(tree);
    if 1: print('DEBUG: --\ntree_have:', tree_have, '\nvisit_have:', visit_have)
    assert tree_have == visit_have

    ## nice -- we can return the result and not squirrel it away in a global
    iter_have = demo_iter(tree); 
    if 1: print('DEBUG: --\ntree_have:', tree_have, '\niter_have:', iter_have)
    assert tree_have == visit_have

main()

[]
