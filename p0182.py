import matplotlib.pyplot as plt
import numpy as np

n = 5
data1 = np.array(range(n)) + np.random.rand(n)
data2 = (np.array(range(n)) + np.random.rand(n)) / 2

fig, ax = plt.subplots(2)

bar_width = 0.4  # default: 0.8
bar_locations = np.arange(n)

ax[0].bar(bar_locations, data1, bar_width)
ax[0].bar(
	bar_locations - bar_width, 
	data2, 
	bar_width, 
	color='r'
)

ax[1].bar(bar_locations, data1, bar_width)
ax[1].bar(
	bar_locations - (bar_width / 2), 
	data2, bar_width, 
	color='r'
)

fig.show()
"""(
![Plot](/assets/img/pp/patterns/p0182_1.png "output")
)"""
