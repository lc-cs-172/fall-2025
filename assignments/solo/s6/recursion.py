"""Recursion exercises adapted from the CodingBat code practice web
pages https://codingbat.com/java/Recursion-1 developed by Nick Parlante.

"""

__author__ = 'Put your name here'

def count_pairs(s : str) -> int:

    """We'll say that a "pair" in a string is two instances of a char
    separated by a char.  So 'AxA' the A's make a pair.  Pair's can
    overlap, so 'AxAxA' contains 3 pairs -- 2 for A and 1 for
    x.  Recursively compute the number of pairs in the given string.

    count_pairs('axa') → 1
    count_pairs('axax') → 2
    count_pairs('axbx') → 1
    """

    return 1

def count_abc(s : str) -> int:

    """Count recursively the total number of 'abc' and 'aba' substrings
    that appear in the given string.

    count_abc('abc') → 1
    count_abc('abcxxabc') → 2
    count_abc('abaxxaba') → 2
    """

    return 1

def count_11(s : str) -> int:

    """Given a string, compute recursively (no loops) the number of '11'
    substrings in the string.  The '11' substrings should not overlap.

    count_11('11abc11') → 2
    count_11('abc11x11x11') → 3
    count_11('111') → 1
    """

    return 1

def string_clean(s : str) -> str:

    """Given a string, return recursively a "cleaned" string where
    adjacent chars that are the same have been reduced to a single
    char.  So 'yyzzza' yields 'yza'.

    string_clean('yyzzza') → 'yza'
    string_clean('abbbcdd') → 'abcd'
    string_clean('Hello') → 'Helo'
    """

    return ''

def count_hi2(s : str) -> int:

    """Given a string, compute recursively the number of times lowercase
    "hi" appears in the string, however do not count "hi" that have an
    'x' immedately before them.

    count_hi2('ahixhi') → 1
    count_hi2('ahibhi') → 2
    count_hi2('xhixhi') → 0

    """

    return ''

def paren_bit(s : str) -> str:

    """Given a string that contains a single pair of parenthesis, compute
    recursively a new string made of only of the parenthesis and their
    contents, so 'xyz(abc)123' yields '(abc)'.

    paren_bit('xyz(abc)123') → '(abc)'
    paren_bit('x(hello)') → '(hello)'
    paren_bit('(xy)1') → '(xy)'
    """

    return ''

def nest_paren(s : str) -> bool:

    """Given a string, return true if it is a nesting of zero or more
    pairs of parenthesis, like '(())' or '((()))'.  Suggestion: check
    the first and last chars, and then recur on what's inside them.

    nest_paren('(())') → True
    nest_paren('((()))') → True
    nest_paren('(((x))') → False
    """

    return False

def str_count(s : str, sub : str) -> int:

    """Given a string and a non-empty substring `sub`, compute recursively
    the number of times that `sub` appears in the string, without the
    `sub` strings overlapping.

    str_count('catcowcat', 'cat') → 2
    str_count('catcowcat', 'cow') → 1
    str_count('catcowcat', 'dog') → 0
    """

    return 1

def str_copies(s : str, sub : str, n : int) -> bool:
    """Given a string and a non-empty substring `sub`, compute recursively
    if at least `n` copies of `sub` appear in the string somewhere,
    possibly with overlappings.  `n` will be non-negative.

    str_copies('catcowcat', 'cat', 2) → True
    str_copies('catcowcat', 'cow', 2) → False
    str_copies('catcowcat', 'cow', 1) → True
    """

    return False

def str_dist(s : str, sub : str) -> int:
    """Given a string and a non-empty substring `sub`, compute recursively
    the largest substring which starts and ends with `sub` and return
    its length.

    str_dist('catcowcat', 'cat') → 9
    str_dist('catcowcat', 'cow') → 3
    str_dist('cccatcowcatxx', 'cat') → 9
    """

    return 0
