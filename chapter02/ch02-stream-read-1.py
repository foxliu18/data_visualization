#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-12-16 下午11:10
# @Author  : liu
# @Project : DataVisualization
# @File    : ch02-stream-read-1.py
# @Software: PyCharm
import struct
import string

datafile = './data/ch02-fixed-width-1M.data'

# this is where we define how to
# understand line of data from the file
mask = '9s14s5s'


def main():
    with open(datafile, 'r') as f:
        for line in f:
            try:
                fields = struct.Struct(bytes(mask, encoding='utf-8')).unpack_from(bytes(line, encoding='utf-8'))
                print('fields:', [field.strip() for field in fields])
            except struct.error as e:
                print('Error:', e.args)


if __name__ == '__main__':
    main()
