#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 05.01.19 12:59
# @Author  : liu
# @Project : DataVisualization
# @File    : ch03_axis_scale.py
# @Software: PyCharm
from pylab import *
import matplotlib as plt
import datetime


if __name__ == '__main__':
    fig = figure()

    # get current axis
    ax = gca()

    # set some daterange
    start = datetime.datetime(2013, 1, 1)
    stop = datetime.datetime(2013, 12, 31)
    delta = datetime.timedelta(days=1)

    # convert dates for matplotlib
    dates = mpl.dates.drange(start, stop, delta)

    # generate some random values
    values = np.random.rand(len(dates))

    ax = gca()

    # create plot with dates
    ax.plot_date(dates, values, fmt='-')

    # specify formatter
    date_format = mpl.dates.DateFormatter('%Y-%m-%d')

    # apply formatter
    ax.xaxis.set_major_formatter(date_format)

    fig.autofmt_xdate()

    show()
