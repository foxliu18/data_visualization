# -*- coding: utf-8 -*-
# @Time    : 4/13/19
# @Author  : lkx-rog
# @Project : data_visualization
# @File    : ch04_my_style
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np
print(plt.style.available)
plt.style.use('mystyle')


def main():
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    plt.title('sin(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    plt.show()


if __name__ == '__main__':
    main()
