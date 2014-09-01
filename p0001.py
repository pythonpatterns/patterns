# split based on whitespace:

a = 'a b    c d  '.split()  # ['a', 'b', 'c', 'd']


# specify a delimiter:

a = 'a |b||c|d'.split('|')  # ['a ', 'b', '', 'c', 'd']


# omit whitespace and empty strings:

a = [s.strip() for s in 'a ,b,,c,d'.split(',') if s.strip()]  # ['a', 'b', 'c', 'd']


# no more than 3 splits:

a = 'a|b|c|d|e'.split('|', 3)  # ['a', 'b', 'c', 'd|e']


# starting from the end:

a = 'a|b|c|d|e'.rsplit('|', 3)  # ['a|b', 'c', 'd', 'e']


# split at the first occurence of the delimiter. Return 3-Tuple:

u, s, d = 'bob@example.com'.partition('@')  # 'bob', '@', 'example.com'


# starting from the end:

f, s, l = 'Bob M. Robertson'.rpartition(' ')  # 'Bob M.', ' ', 'Robertson'
