# -*- coding: utf-8 -*-
# @Time    : 3/14/19
# @Author  : lkx-rog
# @Project : data_visualization
# @File    : ch04_sub_figure
# @Software: PyCharm
import matplotlib.pyplot as plt


def main():
    plt.figure(0)
    axes1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
    axes2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
    axes3 = plt.subplot2grid((3, 3), (1, 2))
    axes4 = plt.subplot2grid((3, 3), (2, 0))
    axes5 = plt.subplot2grid((3, 3), (2, 1), colspan=2)

    # tidy up tick labels size
    all_axes = plt.gcf().axes
    for ax in all_axes:
        for ticklabel in ax.get_xticklabels() + ax.get_yticklabels():
            ticklabel.set_fontsize(10)

    plt.suptitle("Demo of subplot2grid")
    plt.show()


if __name__ == '__main__':
    main()
