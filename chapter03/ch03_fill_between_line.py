#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 12.01.19 23:30
# @Author  : liu
# @Project : DataVisualization
# @File    : ch03_fill_between_line.py
# @Software: PyCharm
from matplotlib.pyplot import figure, show, gca
import numpy as np


def main():
    x = np.arange(0.0, 2, 0.01)

    # two different signals are measured
    y1 = np.sin(2*np.pi*x)
    y2 = 1.2*np.sin(4*np.pi*x)

    fig = figure()
    ax = gca()

    # plot and fill between y1 and y2 where a logical condition is met
    ax.plot(x, y1, x, y2, color='black')

    ax.fill_between(x, y1, y2, where=y2 > y1, facecolor='darkblue', interpolate=True)
    ax.fill_between(x, y1, y2, where=y1 > y2, facecolor='deeppink', interpolate=True)

    ax.set_title('filled between')

    show()


if __name__ == '__main__':
    main()
