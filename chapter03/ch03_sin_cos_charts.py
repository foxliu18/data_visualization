#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 23.12.18 18:09
# @Author  : liu
# @Project : DataVisualization
# @File    : ch03_sin_cos_charts.py
# @Software: PyCharm
from pylab import *
import numpy as np


if __name__ == '__main__':
    # generate uniformly distributed
    # 256 points from -pi to pi, inclusive
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)

    # these are vectorised versions
    # of math.cos, and math.sin in built-in Python maths
    # compute cos for every x
    y = np.cos(x)

    # compute sin for every x
    y1 = np.sin(x)

    # plot cos
    plot(x, y)

    # plot sin
    plot(x, y1)

    # defined plot title
    title("Function $\sin$ and $\cos$")

    # set x limit
    xlim(-3.0, 3.0)
    # set y limit
    ylim(-1.0, 1.0)

    # format ticks at specific values
    xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])
    show()
