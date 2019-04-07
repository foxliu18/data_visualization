# -*- coding: utf-8 -*-
# @Time    : 3/30/19
# @Author  : lkx-rog
# @Project : data_visualization
# @File    : ch04_contour_plot
# @Software: PyCharm

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def process_signals(x, y):
    return (1 - (x ** 2 +y ** 2)) * np.exp(-y ** 3 / 3)


def main():
    x = np.arange(-1.5, 1.5, 0.1)
    y = np.arange(-1.5, 1.5, 0.1)

    # Make grids of points
    X, Y = np.meshgrid(x, y)

    Z = process_signals(X, Y)

    # Number of isolation
    N = np.arange(-1, 1.5, 0.5)

    # adding the contour line with labels
    CS = plt.contour(Z, N, linewidths=2, cmap=mpl.cm.jet)
    plt.clabel(CS, inline=True, fmt='%1.1f', fontsize=10)
    plt.colorbar(CS)

    plt.title('My function : $z=(1-x^2+y^2 e^{-(y^3)/3})$')
    plt.show()


if __name__ == '__main__':
    main()