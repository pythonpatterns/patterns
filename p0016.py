def func(x):
    print(x)
    
def func_2(x):
    return 2*x
    
a = [1, 2, 3, 4]
map(func, a)
"""<
1
2
3
4
>"""
b = map(func_2, a)
print(b)
"""<
[2, 4, 6, 8]
>"""
c = [func_2(x) for x in a]
print(c)
"""<
[2, 4, 6, 8]
>"""
