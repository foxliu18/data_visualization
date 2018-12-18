#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18.12.18 21:28
# @Author  : liu
# @Project : DataVisualization
# @File    : ch02-dirty-tabread.py
# @Software: PyCharm

datafile = './data/ch02-data-dirty.tab'


def main():
    with open(datafile, 'r') as f:
        for line in f:
            # remove next comment to see line before cleanup
            print('DIRTY:', line.split('\t'))

            # we remove any space in line start or end
            line = line.strip()

            # now we split the line by tab delimiter
            print('CLEAN', line.split('\t'))


if __name__ == '__main__':
    main()
