import matplotlib.pyplot as plt

# Sample data:
x = range(0, 13) 
y = [[i * j for i in x] for j in x]

# Blue (default):
plt.plot(x, y[11])
plt.plot(x, y[10], 'b')
plt.plot(x, y[9], 'blue')
plt.plot(x, y[8], color='b')
plt.plot(x, y[7], '#0000ff')

# Some of the other options:
plt.plot(x, y[6], 'g')
plt.plot(x, y[5], 'r')
plt.plot(x, y[4], 'c')
plt.plot(x, y[3], 'm')
plt.plot(x, y[2], 'y')
plt.plot(x, y[1], 'k')

plt.show()
"""(
![Plot](/assets/img/pp/patterns/p0143_1.png "output")
)"""