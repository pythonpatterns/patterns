import matplotlib.pyplot as plt

x = (1, 2, 3, 4, 5, 6)
h = (3, 2, 5, 1, 4, 0.5)

plt.bar(x, h)
plt.show()
"""(
![Plot](/assets/img/pp/patterns/p0146_1.png "output")
)"""
plt.barh(x, h)
plt.show()
"""(
![Plot](/assets/img/pp/patterns/p0146_2.png "output")
)"""
plt.bar(
    x, 
    h,
    width=0.5,
    color='#624ea7',
    linewidth=2.0
)
plt.show()
"""(
![Plot](/assets/img/pp/patterns/p0146_3.png "output")
)"""
plt.bar(
    x, 
    h,
    color=('m', 'c', 'm', 'm', 'k', 'm'),
    edgecolor=('k', 'k' , 'k', 'k', 'c', 'k'),
    linewidth=(1, 2, 1, 1, 2, 1),
    align='center'
)
plt.show()
"""(
![Plot](/assets/img/pp/patterns/p0146_4.png "output")
)"""