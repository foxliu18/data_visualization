#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 12.01.19 16:32
# @Author  : liu
# @Project : DataVisualization
# @File    : ch03_hist.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt

mu = 100
sigma = 1.5


def main():
    x = np.random.normal(mu, sigma, 10000)
    ax = plt.gca()

    # the histogram of the data
    ax.hist(x, bins=35, color='r')

    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')

    ax.set_title(r'$\mathrm{Histogram:}\ \mu=%d, \ \sigma=%d$' % (mu, sigma))

    plt.show()


if __name__ == '__main__':
    main()
