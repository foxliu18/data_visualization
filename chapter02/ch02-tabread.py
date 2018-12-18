#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18-12-16 下午11:35
# @Author  : liu
# @Project : DataVisualization
# @File    : ch02-tabread.py
# @Software: PyCharm
import csv
import sys

filename = './data/ch02-data.tab'


def main():
    try:
        with open(filename) as f:
            reader = csv.reader(f, dialect=csv.excel_tab)
            header = next(reader)
            data = [row for row in reader]
    except csv.Error as e:
        print('Error reading CSV file at line %s: %s' % (reader.line_num, e))
        sys.exit(-1)

    if header:
        print(header)
        print('====================')

    for datarow in data:
        print(datarow)


if __name__ == '__main__':
    main()
