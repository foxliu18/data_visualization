#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 12.01.19 16:46
# @Author  : liu
# @Project : DataVisualization
# @File    : ch03_error_bar.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt


def main():
    # generate number of measurement
    x = np.arange(0, 10, 1)

    # values computed from "measured"
    y = np.log(x)

    # add some error samples from standard normal distribution
    xe = 0.1 * np.abs(np.random.randn(len(y)))

    # draw and show errorbar
    plt.bar(x, y, yerr=xe, width=0.4, align='center', ecolor='r', color='cyan', label='experiment #1');

    # give some explainations
    plt.xlabel('# measurement')
    plt.ylabel('Measurd values')
    plt.title('Measurements')
    plt.legend(loc='upper left')

    plt.show()


if __name__ == '__main__':
    main()
