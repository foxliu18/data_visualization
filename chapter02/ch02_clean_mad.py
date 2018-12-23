#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 23.12.18 01:38
# @Author  : liu
# @Project : DataVisualization
# @File    : ch02_clean_mad.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt


def is_outlier(points, threshold=3.5):
    """
    This returns a boolean array with "True" if points are outliers and "False"
    otherwise
    There are the data points with a modified z-zeros greater than this:
    # value will be classified as outliers.
    :param points:
    :param threshold:
    :return:
    """
    # transform into vector
    if len(points.shape) == 1:
        points = points[:, None]

    # compute median value
    median = np.median(points, axis=0)

    # compute diff sums along the axis
    diff = np.sum((points - median)**2, axis=-1)
    diff = np.sqrt(diff)
    # computer MAD
    med_abs_deviation = np.median(diff)

    # compute modified Z-score
    modified_z_score = 0.6745 * diff / med_abs_deviation

    # return a mask for each outlier
    return modified_z_score > threshold


def main():
    # Random data
    x = np.random.random(100)

    # histogram buckets
    buckets = 50

    # Add in a few outliers
    x = np.r_[x, -49, 95, 100, -100]

    # Keep valid data points
    # Note here that
    # '~' is logical NOT on boolean numpy arrays
    filtered = x[~is_outlier(x)]
    # plot histogram
    plt.figure()
    plt.subplot(211)
    plt.hist(x, buckets)
    plt.xlabel('Raw')

    plt.subplot(212)
    plt.hist(filtered, buckets)
    plt.xlabel('Cleaned')

    plt.show()


if __name__ == '__main__':
    main()
