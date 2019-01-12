#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 05.01.19 13:26
# @Author  : liu
# @Project : DataVisualization
# @File    : ch03_legend_annotate.py
# @Software: PyCharm
from matplotlib.pyplot import *


def main():

    # generate different normal distributions
    x1 = np.random.normal(30, 3, 100)
    x2 = np.random.normal(20, 2, 100)
    x3 = np.random.normal(10, 3, 100)

    # plot them
    plot(x1, label='plot')
    plot(x2, label='2nd plot')
    plot(x3, label='last plot')

    # generate a legend box
    legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=3, mode="expand", borderaxespad=0.)

    # annotate an important value
    annotate("Important value", (55, 20), xycoords="data", xytext=(5, 38),
             arrowprops=dict(arrowstyle='->'))
    show()


if __name__ == '__main__':
    main()
