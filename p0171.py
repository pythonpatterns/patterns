import matplotlib.pyplot as plt
import numpy as np

n = 50
x = np.random.randn(n)
y = x * np.random.randn(n)

fig, ax = plt.subplots(2, figsize=(6, 6))

ax[0].scatter(x, y, s=50)

sizes = (np.random.randn(n) * 8) ** 2
ax[1].scatter(x, y, s=sizes)

fig.show()
"""(
![Plot](/assets/img/pp/patterns/p0171_1.png "output")
)"""
