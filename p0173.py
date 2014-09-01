import matplotlib.pyplot as plt
import numpy as np

n = 50
x = np.random.randn(n)
y = x * np.random.randn(n)

fig, ax = plt.subplots(2, figsize=(6, 6))

all_markers = [
    'o', 
    'v', 
    '^', 
    '<', 
    '>', 
    '1', 
    '2', 
    '3', 
    '4', 
    '8', 
    's', 
    'p', 
    'h', 
    'H', 
    'd', 
    'D', 
    '+', 
    'x', 
    '*', 
    '|', 
    '_'
]
ax[0].scatter(x, y, marker=all_markers[15], s=80)
ax[1].scatter(x, y, marker=all_markers[1], s=80)

fig.show()
"""(
![Plot](/assets/img/pp/patterns/p0173_1.png "output")
)"""
