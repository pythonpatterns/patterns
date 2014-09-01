import matplotlib.pyplot as plt

a = [1, 2, 3, 4]
b = [2, 4, 6, 8]

plt.plot(a, b)

plt.savefig('test.png', dpi=90)
