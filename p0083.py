from pprint import pprint
from itertools import permutations as perm

a = ['a', 'b', 'c']

b = list(perm(a))  
pprint(b)
"""<
[('a', 'b', 'c'),
 ('a', 'c', 'b'),
 ('b', 'a', 'c'),
 ('b', 'c', 'a'),
 ('c', 'a', 'b'),
 ('c', 'b', 'a')]
>"""
c = [''.join(p) for p in perm(a)]  
print(c)
"""<
['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
>"""
d = [''.join(p) for p in perm(a, 2)]  
print(d)
"""<
['ab', 'ac', 'ba', 'bc', 'ca', 'cb']
>"""
