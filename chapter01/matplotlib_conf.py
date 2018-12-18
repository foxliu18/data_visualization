# -*- coding: utf-8 -*-
# @Time    : 09.12.18 15:30
# @Author  : liu
# @Project : DataVisualization
# @File    : matplotlib_conf.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    t = np.arange(0.0, 1.0, 0.01)

    s = np.sin(2*np.pi*t)
    # 设置线条颜色为红色
    plt.rcParams['lines.color'] = 'r'
    plt.plot(t, s)

    c = np.cos(2*np.pi*t)
    # 设置线宽
    plt.rcParams['lines.linewidth'] = '5'
    plt.plot(t, c)

    plt.show()
