import numpy as np

a = np.random.standard_normal()
print(a)
"""<
2.02257203322
>"""
b = np.random.standard_normal(5)
print(b)
"""<
[-0.94111007 -1.8384039   2.16157696  0.56518711 -0.95918094]
>"""
b = np.random.standard_normal((3,3))
print(b)
"""<
[[ 1.31135088 -0.19896956 -2.04799324]
 [ 0.01238043  0.29975329 -0.34229102]
 [ 1.67252777  2.83222642 -0.19889494]]
>"""
