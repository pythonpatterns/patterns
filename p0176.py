import matplotlib.pyplot as plt
import numpy as np

n = 5
data = np.array(range(n)) + np.random.rand(n)

fig, ax = plt.subplots()

bar_width = 0.4  # default: 0.8
bar_locations = np.arange(n)
ax.bar(bar_locations, data, bar_width)

fig.show()
"""(
![Plot](/assets/img/pp/patterns/p0176_1.png "output")
)"""