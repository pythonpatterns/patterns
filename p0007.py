a = ['a', 'c', 'd', 'b']

b = sorted(a, reverse=True)
print(b)
"""<
['d', 'c', 'b', 'a']
>"""
print(a)
"""<
['a', 'c', 'd', 'b']
>"""
a.sort(reverse=True)
print(a)
"""<
['d', 'c', 'b', 'a']
>"""
