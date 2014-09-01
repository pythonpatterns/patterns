import matplotlib.pyplot as plt
import numpy as np

n = 5
data = np.array(range(n)) + np.random.rand(n)

fig, ax = plt.subplots(7, figsize=(6, 18))

bar_locations = np.arange(n)
ax[0].bar(bar_locations, data)
ax[1].bar(bar_locations, data, linewidth=4.0)
ax[2].bar(bar_locations, data, linewidth=[1.0, 4.0])

line_widths = [4.0 if i == 3 else None for i in range(n)]
ax[3].bar(bar_locations, data, linewidth=line_widths)

ax[4].bar(bar_locations, data, edgecolor='red', linewidth=4.0)

ax[5].bar(
	bar_locations, 
	data, 
	edgecolor=['red', 'black'], 
	linewidth=4.0
)

edge_colors = ['#624ea7', 'g', 'yellow', 'k', 'maroon']
ax[6].bar(
	bar_locations, 
	data, 
	edgecolor=edge_colors, 
	linewidth=4.0
)

fig.show()
"""(
![Plot](/assets/img/pp/patterns/p0179_1.png "output")
)"""
