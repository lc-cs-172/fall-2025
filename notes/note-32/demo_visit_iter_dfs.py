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

    ## simplified iterator using 'yield from' syntax
    def __iter__(self):
        if self.left: yield from iter(self.left)
        yield self
        if self.right: yield from iter(self.right)

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

##================================================================
## ====    ====    ====   New and Improved   ====    ====    ====
##================================================================

def demo_visit_easy(tree):
    'demo how this works; we explicitly accumulate the visits in our local storage'
    my_visit_have = []
    def my_visitor(item):
        my_visit_have.append(item) # magic!  no need to declare nonlocal since not doing "assignment"
    tree.visit(my_visitor)
    return my_visit_have

##================================================================

##----------------------------------------------------------------

def demo_iter(tree):
    'demo how we can use an iterator to visit each item when we want to'
    'NB: we control the flow of execution -- we call the iterator when we want another'
    result = []
    for key in iter(tree):
        result.append(key)
    return result

##----------------------------------------------------------------

##================================================================
## DFS -- Depth First Search
##================================================================

##==========================================================
## NB: This is NOT the conventional definition of depth.
##     We are counting the number of NODES, not edges,
##     on the longest path from root to leaf.
##=================================
##     depth(<empty-tree>) == 0
##     depth(<root-only>)  == 1
##=================================

def dfs_max_depth(tree):
    "return the maximum depth in the tree"
    return dfs_node_depth(tree._root, 1)

def dfs_node_depth(node, depth):
    if not node: return 0
    left = dfs_node_depth(node.left, depth+1)
    right = dfs_node_depth(node.right, depth+1)
    return max(depth, left, right)

##================================================================

##----------------------------------------------------------------

TREE_BEST = 0
TREE_VINE = 1
TREE_SKEW = 2
TREE_RAND = 3

import random

def build_subtree(lo, hi, mode = TREE_BEST):
    "return subtree build from integers [lo,hi)"
    """
    KISS: This is test code -- with restricted usage --
    if we are building a balanced BST,
    we just cut in half each time.
    """
    debug = 0
    size = hi-lo
    if 0 == size: return None
    if 1 == size: return Node(lo)

    if   mode == TREE_BEST:
        split = (lo+hi)//2
    elif mode == TREE_VINE:
        split = lo
    elif mode == TREE_SKEW:
        split = (2*lo+hi)//3
    elif mode == TREE_RAND:
        split = random.randint(lo,hi-1)
    else:
        assert False, 'mode is expected value'
    if debug: print('DEBUG: (lo, hi, split):', (lo, hi, split))
        
    root = Node(split)
    root.left = build_subtree(lo,split,mode)
    ## I am not a huge Python fan ... I had a typo, "rigth", w/ silent failure
    root.right = build_subtree(split+1,hi,mode)
    if debug: print(f'DEBUG: built subtree {root}')
    return root

##----------------------------------------------------------------

def dump_tree(node, width):
    "crude, but good enough for debugging"
    glue = (width-2) // 2
    fill = ' ' * glue
    if node:
        my_line = fill +  f'{node.key:02d}' + fill
        side1 = dump_tree(node.left,  width//2)
        side2 = dump_tree(node.right, width//2)

        ## ensure we see all of both sides, since zip stops at shortest
        gap = abs( len(side1) - len(side2) )
        dummy = fill + '.'
        padding = [ dummy for _ in range(gap) ]
        side1 += padding
        side2 += padding

        my_rest = [ half1 + half2 for (half1,half2) in zip(side1, side2) ]
        return [my_line] + my_rest

    else:        
        return [ fill + '[]' + fill ]

def print_tree_dump(lump):
    for line in lump:
        print(line)

##----------------------------------------------------------------

tree = None     # make it a global, so it's easy to inspect interactively

def main():
    global tree
    lo = 1
    hi = 16
    tree_have = [ i for i in range(lo,hi) ] # what we put in the tree

    tree = Tree()                        # working tree we muck with 
    tree._root = build_subtree(lo,hi)    # testing code -- stuff in tree
    print_tree_dump(dump_tree(tree._root, 96))

    demo_visit(tree);
    if 1: print('DEBUG: --\ntree_have:', tree_have, '\nvisit_have:', visit_have)
    assert tree_have == visit_have

    ## let's do it the easy way!
    easy_visit_have = demo_visit_easy(tree)
    if 1: print('DEBUG: --\ntree_have:', tree_have, '\neasy_visit_have:', easy_visit_have)
    assert tree_have == easy_visit_have

    ## nice -- we can return the result and not squirrel it away in a global
    iter_have = demo_iter(tree); 
    if 1: print('DEBUG: --\ntree_have:', tree_have, '\niter_have:', iter_have)
    assert tree_have == iter_have

    ## bonus: show how dfs works
    depth = dfs_max_depth(tree)
    if 1: print('DEBUG: dfs_max_depth(BEST_tree):', depth)
    assert 4 == depth

    ## bonus: show how dfs works
    tree._root = build_subtree(lo,hi,TREE_VINE)    # testing code -- stuff in new tree
    depth = dfs_max_depth(tree)
    if 1: print('DEBUG: dfs_max_depth(VINE_tree):', depth)
    assert 15 == depth

    ## bonus: show how dfs works
    tree._root = build_subtree(lo,hi,TREE_SKEW)    # testing code -- stuff in new tree
    print_tree_dump(dump_tree(tree._root, 96))
    depth = dfs_max_depth(tree)
    if 1: print('DEBUG: dfs_max_depth(SKEW_tree):', depth)
    assert 5 == depth

main()

[]
