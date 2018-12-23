#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 23.12.18 12:50
# @Author  : liu
# @Project : DataVisualization
# @File    : ch02_imshow_lena.py
# @Software: PyCharm
import numpy
from PIL import Image
import matplotlib.pyplot as plt


if __name__ == '__main__':
    bug = Image.open('./data/stinkbug.png')
    arr = numpy.array(bug.getdata(), numpy.uint8).reshape(bug.size[1], bug.size[0], 3)

    plt.gray()
    plt.imshow(arr)
    plt.colorbar()
    plt.show()
