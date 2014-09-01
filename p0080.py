a = 'a ,b,,c,d'

b = [s.strip() for s in a.split(',') if s.strip()]
print(b)
"""<
['a', 'b', 'c', 'd']
>"""
