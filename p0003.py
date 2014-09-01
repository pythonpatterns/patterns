a = ['a', 'B', 'C', 'd']

b = sorted(a, key=lambda x: x.lower())
print(b)
"""<
['a', 'B', 'C', 'd']
>"""
"""(
OR sort in place:
)"""
a.sort(key=lambda s: s.lower())
print(a)
"""<
['a', 'B', 'C', 'd']
>"""
"""(
If the list might contain non-string elements:
)"""
def lc(s):
    try:
        return s.lower()
    except AttributeError:
        return s

c = ['a', 'B', 1, 'C', 'd']
    
d = sorted(c, key=lc)
print(d)
"""<
[1, 'a', 'B', 'C', 'd']
>"""
