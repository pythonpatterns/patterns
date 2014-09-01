import matplotlib.pyplot as plt
import numpy as np

n = 5
data1 = np.array(range(n)) + np.random.rand(n)
data2 = np.random.rand(n) + 1

fig, ax = plt.subplots()

bar_locations = np.arange(n)
ax.bar(bar_locations, data1)
ax.bar(bar_locations, data2, bottom=data1, color='r')

fig.show()
"""(
![Plot](/assets/img/pp/patterns/p0180_1.png "output")
)"""