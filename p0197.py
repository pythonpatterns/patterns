def flatten_dict(d, delimiter='.'):
    def expand(key, value):
        if isinstance(value, dict):
            return [
                (delimiter.join([key, k]), v)
                for k, v in flatten_dict(value, delimiter).items()
            ]
        else:
            return [(key, value)]
    return dict([item for k, v in d.items() for item in expand(k, v)])

"""(
<br />
#### Examples
)"""
a = {
    'a': 1,
    'b': {
        'a': 21,
        'b': {
            'a': 221,
        },
        'c': 23,
    },
    'd': 4,
}

b = flatten_dict(a)
print(b)
"""<
{'a': 1, 'b.c': 23, 'b.a': 21, 'b.b.a': 221, 'd': 4}
>"""
c = flatten_dict(a, '->')
print(c)
"""<
{'a': 1, 'b->a': 21, 'b->c': 23, 'b->b->a': 221, 'd': 4}
>"""
