# -*- coding: utf-8 -*-
# @Time    : 10.12.18 10:50
# @Author  : liu
# @Project : DataVisualization
# @File    : ch02_csv_writer.py
# @Software: PyCharm
import csv

if __name__ == '__main__':
    filename = './data/ch02-data-write.csv'

    # we open file with 'b' flag
    # for compatibility with non-linux users
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for row in range(10):
            writer.writerow([row + 1, '2012-01-%s' % (19 + row)])
