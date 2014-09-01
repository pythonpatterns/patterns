import matplotlib.pyplot as plt

# Sample data:
x = range(1, 11) 
y = [[i * j for i in x] for j in x]

# Solid line (default):
plt.plot(x, y[9])
plt.plot(x, y[8], '-')
plt.plot(x, y[7], linestyle='-')

# Some of the other options:
plt.plot(x, y[6], '--')
plt.plot(x, y[5], ':')
plt.plot(x, y[4], 'o')
plt.plot(x, y[3], 'v')
plt.plot(x, y[2], '*')
plt.plot(x, y[1], ':')
plt.plot(x, y[0], 'D')

plt.show()
"""(
![Plot](/assets/img/pp/patterns/p0142_1.png "output")
)"""
