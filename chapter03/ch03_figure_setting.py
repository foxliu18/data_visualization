#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 23.12.18 17:47
# @Author  : liu
# @Project : DataVisualization
# @File    : ch03_figure_setting.py
# @Software: PyCharm
from matplotlib.pyplot import *
# some simple data
x = [1, 2, 3, 4]
y = [5, 4, 3, 2]
# create new figure


def main():
    figure("sample charts")
    # divide subplots into 2 x 3 grid
    # add select #1
    subplot(231)
    plot(x, y)

    # select #2
    subplot(232)
    bar(x, y)

    # horizontal bar-charts
    subplot(233)
    barh(x, y)

    # create stacked bar charts
    subplot(234)
    bar(x, y)

    # we need more data for stacked bar charts
    y1 = [7, 8, 5, 3]
    bar(x, y1, bottom=y, color='r')

    # box plot
    subplot(235)
    boxplot(x)

    # scatter plot
    subplot(236)
    scatter(x, y)

    show()


if __name__ == '__main__':
    main()

