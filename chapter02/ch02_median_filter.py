#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 23.12.18 17:08
# @Author  : liu
# @Project : DataVisualization
# @File    : ch02_median_filter.py
# @Software: PyCharm
import numpy as np
import pylab as p
from scipy import signal as signal


def main():
    # get some linear data
    x = np.linspace(0, 1, 101)

    # add some noisy signal
    x[3::10] = 1.5

    p.plot(x)
    p.plot(signal.medfilt(x, 3))
    p.plot(signal.medfilt(x, 5))

    p.legend(['original signal', 'length 3', 'length 5'])
    p.show()


if __name__ == '__main__':
    main()
