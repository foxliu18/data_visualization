# -*- coding: utf-8 -*-
# @Time    : 3/30/19
# @Author  : lkx-rog
# @Project : data_visualization
# @File    : ch04_fill_between
# @Software: PyCharm

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.arange(0.0, 2, 0.01)
    y1 = np.sin(np.pi*x)
    y2 = 1.7*np.sin(4*np.pi*x)

    fig = plt.figure()
    axesl = fig.add_subplot(211)
    axesl.plot(x, y1, x, y2, color='grey')
    axesl.fill_between(x, y1, y2, where=y2 <= y1, facecolor='blue', interpolate=True)
    axesl.fill_between(x, y1, y2, where=y2 >= y1, facecolor='gold', interpolate=True)
    axesl.set_title('Blue where y2 <= y1. Gold-color where u2 >= y1.')
    axesl.set_ylim(-2, 2)

    # Mask values in y2 with greeter than 1.0
    y2 = np.ma.masked_greater(y2, 1.0)
    axes2 = fig.add_subplot(212, sharex=axesl)
    axes2.plot(x, y1, x, y2, color='black')
    axes2.fill_between(x, y1, y2, where=y2 <= y1, facecolor='blue', interpolate=True)
    axes2.fill_between(x, y1, y2, where=y2 >= y1, facecolor='gold', interpolate=True)
    axes2.set_title('Same as above, but mask')
    axes2.set_ylim(-2, 2)
    axes2.grid('on')

    plt.show()


if __name__ == '__main__':
    main()