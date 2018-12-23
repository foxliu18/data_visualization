#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 23.12.18 15:23
# @Author  : liu
# @Project : DataVisualization
# @File    : ch02_random_noise.py
# @Software: PyCharm
import pylab
import random
import matplotlib
from matplotlib import pyplot as plt


SAMPLE_SIZE = 1000
# histogram buckets
buckets = 100

plt.figure()

# we need to update font size just for this example
matplotlib.rcParams.update({'font.size': 7})


def price_distribution():
    # days to generate data for
    duration = 100
    # mean value
    mean_inc = 0.0

    # standard deviation
    std_dev_inc = 1.2

    # time series
    x = range(duration)
    y = []
    price_today = 0

    for i in x:
        next_delta = random.normalvariate(mean_inc, std_dev_inc)
        price_today += next_delta
        y.append(price_today)

    pylab.plot(x, y)
    pylab.xlabel('Time')
    pylab.ylabel('Value')
    pylab.show()


if __name__ == '__main__':
    # price_distribution()
    plt.subplot(621)
    plt.xlabel("random.random")
    # Return the next random floating point number in the range [0.0, 1.0)
    res = [random.random() for _ in range(1, SAMPLE_SIZE)]
    plt.hist(res, buckets)

    plt.subplot(622)
    plt.xlabel("random.uniform")
    # Return a random floating point number N such that a <= N <= b for a <= b
    # and b <= N <= a for b < a
    # The end-point value b may or may not be included in the range
    # depending on floating-point rounding in the equation a + (b-a) * random()
    a = 1
    b = SAMPLE_SIZE
    res = [random.uniform(a, b) for _ in range(1, SAMPLE_SIZE)]
    plt.hist(res, buckets)

    plt.subplot(623)
    plt.xlabel("random.triangular")

    # Return a random floating point number N such that low <= N <=  high
    # and with the specified
    # mode between those bounds. The low and high bounds default to zero and one.
    # The mode argument defaults to the midpoint between the bounds, giving
    # a symmetrical distribution
    low = 1
    high = SAMPLE_SIZE
    res = [random.triangular(low, high) for _ in range(1, SAMPLE_SIZE)]
    plt.hist(res, buckets)

    # beta distribution
    plt.subplot(624)
    plt.xlabel("random.betavariate")
    alpha = 1
    beta = 10
    res = [random.betavariate(alpha, beta) for _ in range(1, SAMPLE_SIZE)]
    plt.hist(res, buckets)

    # exponential distribution
    plt.subplot(625)
    plt.xlabel("random.exponential")
    lambd = 1.0/((SAMPLE_SIZE + 1) / 2.)
    res = [random.expovariate(lambd) for _ in range(1, SAMPLE_SIZE)]
    plt.hist(res, buckets)

    # gamma distribution
    plt.subplot(626)
    plt.xlabel("random.gammavariate")
    alpha = 1
    beta = 10
    res = [random.gammavariate(alpha, beta) for _ in range(1, SAMPLE_SIZE)]
    plt.hist(res, buckets)

    # log normal distribution
    plt.subplot(627)
    plt.xlabel("random.lognormalvariate")
    mu = 1
    sigma = 0.5
    res = [random.lognormvariate(mu, sigma) for _ in range(1, SAMPLE_SIZE)]
    plt.hist(res, buckets)

    # normal distribution
    plt.subplot(628)
    plt.xlabel("random.normalvariate")
    mu = 1
    sigma = 0.5
    res = [random.normalvariate(mu, sigma) for _ in range(1, SAMPLE_SIZE)]
    plt.hist(res, buckets)

    # pareto distribution
    plt.subplot(629)
    plt.xlabel("random.paretovariate")
    alpha = 1
    res = [random.paretovariate(alpha) for _ in range(1, SAMPLE_SIZE)]
    plt.hist(res, buckets)

    plt.tight_layout()
    plt.show()
