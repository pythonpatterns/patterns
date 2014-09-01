import matplotlib.pyplot as plt
import numpy as np

n = 5
data = np.array(range(n)) + np.random.rand(n)

fig, ax = plt.subplots()

bar_locations = np.arange(n)
ax.bar(bar_locations, data)

fig.show()
"""(
![Plot](/assets/img/pp/patterns/p0175_1.png "output")
)"""