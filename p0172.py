import matplotlib.pyplot as plt
import numpy as np

n = 50
x = np.random.randn(n)
y = x * np.random.randn(n)

fig, ax = plt.subplots(2, figsize=(6, 6))

ax[0].scatter(x, y, c='violet', s=60)

colors = np.random.randn(n)
ax[1].scatter(x, y, c=colors, s=60)

fig.show()
"""(
![Plot](/assets/img/pp/patterns/p0172_1.png "output")
)"""
