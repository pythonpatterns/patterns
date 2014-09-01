import matplotlib.pyplot as plt
import numpy as np

n = 5
data = np.array(range(n)) + np.random.rand(n)

fig, ax = plt.subplots(4, figsize=(6, 12))

bar_locations = np.arange(n)
ax[0].bar(bar_locations, data)
ax[1].bar(bar_locations, data, color='red')

ax[2].bar(bar_locations, data, color=['red', 'blue'])

colors = ['#624ea7', 'g', 'yellow', 'k', 'maroon']
ax[3].bar(bar_locations, data, color=colors)

fig.show()
"""(
![Plot](/assets/img/pp/patterns/p0178_1.png "output")
)"""