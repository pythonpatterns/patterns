"""(
Install the package _matplotlib-venn_:
 
`easy_install matplotlib-venn` or `pip install matplotlib-venn`. 

More information: [https://pypi.python.org/pypi/matplotlib-venn](https://pypi.python.org/pypi/matplotlib-venn)

)"""
from matplotlib import pyplot as plt
from matplotlib_venn import venn2, venn2_circles


# Subset sizes
s = (
    2,  # Ab
    3,  # aB
    1,  # AB
)

v = venn2(subsets=s, set_labels = ('A', 'B'))

# Subset labels
v.get_label_by_id('10').set_text('A but not B')
v.get_label_by_id('01').set_text('B but not A')
v.get_label_by_id('11').set_text('A and B')

# Subset colors
v.get_patch_by_id('10').set_color('c')
v.get_patch_by_id('01').set_color('#993333')
v.get_patch_by_id('11').set_color('blue')

# Subset alphas
v.get_patch_by_id('10').set_alpha(0.4)
v.get_patch_by_id('01').set_alpha(1.0)
v.get_patch_by_id('11').set_alpha(0.7)

# Border styles
c = venn2_circles(subsets=s, linestyle='solid')
c[0].set_ls('dashed')  # Line style
c[0].set_lw(2.0)       # Line width

plt.show()
"""(
![Plot](/assets/img/pp/patterns/p0144_1.png "output")
)"""
