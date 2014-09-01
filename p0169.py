import matplotlib.pyplot as plt
import numpy as np

n = 50
x = np.random.randn(n)
y = x * np.random.randn(n)

fig, ax = plt.subplots()
ax.scatter(x, y)

fig.show()
"""(
![Plot](/assets/img/pp/patterns/p0169_1.png "output")
)"""