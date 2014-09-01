a = ['aaaa', 'B', 'CCC', 'dd']

b = sorted(a, key=lambda x: len(x))
print(b)
"""<
['B', 'dd', 'CCC', 'aaaa']
>"""
print(a)
"""<
['aaaa', 'B', 'CCC', 'dd']
>"""
a.sort(key=lambda x: len(x))
print(a)
"""<
['B', 'dd', 'CCC', 'aaaa']
>"""
