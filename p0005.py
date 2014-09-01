a = ['d', 'C', 'B', 'a']

b = sorted(a, key=lambda x: x.lower())
print(b)
"""<
['a', 'B', 'C', 'd']
>"""
print(a)
"""<
['d', 'C', 'B', 'a']
>"""
a.sort(key=lambda s: s.lower())
print(a)
"""<
['a', 'B', 'C', 'd']
>"""
