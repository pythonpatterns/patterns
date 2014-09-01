"""(
Install the package _matplotlib-venn_:
 
`easy_install matplotlib-venn` or `pip install matplotlib-venn`. 

More information: [https://pypi.python.org/pypi/matplotlib-venn](https://pypi.python.org/pypi/matplotlib-venn)

)"""
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles


# Subset sizes
s = (
    2,    # Abc
    3,    # aBc
    4,    # ABc
    3,    # abC
    1,    # AbC
    0.5,  # aBC
    4,    # ABC
)

v = venn3(subsets=s, set_labels = ('A', 'B', 'C'))

# Subset labels
v.get_label_by_id('100').set_text('Abc')
v.get_label_by_id('010').set_text('aBc')
v.get_label_by_id('110').set_text('ABc')
v.get_label_by_id('001').set_text('Abc')
v.get_label_by_id('101').set_text('aBc')
v.get_label_by_id('011').set_text('ABc')
v.get_label_by_id('111').set_text('ABC')

# Subset colors
v.get_patch_by_id('100').set_color('c')
v.get_patch_by_id('010').set_color('#993333')
v.get_patch_by_id('110').set_color('blue')

# Subset alphas
v.get_patch_by_id('101').set_alpha(0.4)
v.get_patch_by_id('011').set_alpha(1.0)
v.get_patch_by_id('111').set_alpha(0.7)

# Border styles
c = venn3_circles(subsets=s, linestyle='solid')
c[0].set_ls('dotted')  # Line style
c[1].set_ls('dashed')
c[2].set_lw(1.0)       # Line width

plt.show()
"""(
![Plot](/assets/img/pp/patterns/p0145_1.png "output")
)"""