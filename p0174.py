import matplotlib.pyplot as plt
import numpy as np

n = 50
x = np.random.randn(n)
y = x * np.random.randn(n)

fig, ax = plt.subplots(3, figsize=(6, 9))

ax[0].scatter(x, y, alpha=0.1, s=80)
ax[1].scatter(x, y, alpha=0.5, s=80)
ax[2].scatter(x, y, alpha=1, s=80)

fig.show()
"""(
![Plot](/assets/img/pp/patterns/p0174_1.png "output")
)"""
