#! /usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 18.12.18 21:51
# @Author  : liu
# @Project : DataVisualization
# @File    : ch02_write_data.py
# @Software: PyCharm
import os
import sys
import argparse
from io import StringIO
import numpy as np
import struct
import json
import csv


def import_data(import_file):
    """
    Import data from import_file
    Expects to find fixed width row
    Sample row: 161322597 0386544341896 0042
    :param import_file:
    :return:
    """
    mask = '9s14s5s'
    data = []
    with open(import_file, 'r') as f:
        for line in f:
            # unpack line to tuple
            try:
                fields = struct.Struct(mask).unpack_from(bytes(line, encoding='utf-8'))
            except struct.error as e:
                print('Error:', e.args[0])
            # strip any whitespace for each field
            # pack everything in a list and add to full dataset
            data.append(list([f.strip() for f in fields]))
    return data


def write_data(data, export_format):
    """
    Dispatches call to a specific transformer and returns data set.
    Exception is xlsx where we have to save data in a file.
    :param data:
    :param export_format:
    :return:
    """
    if export_format == 'csv':
        return write_csv(data)
    elif export_format == 'json':
        return write_json(data)
    elif export_format == 'xlsx':
        return write_xlsx(data)
    else:
        raise Exception("Illegal format defined")


def write_csv(data):
    """Transforms data into csv.
    Return csv as string.
    """
    # Using this to simulate file IO,
    # as csv can only write to files.
    f = StringIO()
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)
    # Get the content of the file-like object
    return f.getvalue()


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)


def write_json(data):
    """
    Transforms data into json. Very straightforward.
    :param data:
    :return:
    """
    try:
        j = json.dumps(data, cls=MyEncoder)
        return j
    except Exception as e:
        return e.args[0]


def write_xlsx(data):
    """
    Write data into xlsx file.
    :param data:
    :return:
    """
    from xlwt import Workbook
    book = Workbook()
    sheet1 = book.add_sheet("Sheet 1")
    row = 0
    for line in data:
        col = 0
        for datum in line:
            # print(datum)
            try:
                newdatum = []
                for i in datum:
                    print(i)
                    newdatum.append(str(i))
                sheet1.write(row, col, newdatum)
            except Exception as e:
                print(newdatum)
                print(len(newdatum))
                print(e.args[0])
                return None
            col += 1
        row += 1
        if row > 100:
            break
    # XLS is special case where we have to
    # save the file and just return 0
    f = StringIO()
    return f.getvalue()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("import_file", help="Path to a fixed-width data file.")
    parser.add_argument("export_format", help="Export format: json, csv, xlsx.")
    args = parser.parse_args()
    # args.import_file = './data/ch02-fixed-width-1M.data'
    # args.export_format = './data'

    if args.import_file is None:
        print(sys.stderr, "You must specify path to import from.")
        sys.exit(1)

    if args.export_format not in ('csv', 'json', 'xlsx'):
        print(sys.stderr, "You must provide valid export file format.")
        sys.exit(1)

    # verify given path is accessible file
    if not os.path.isfile(args.import_file):
        print(sys.stderr, "Given path is not a file: %s" % args.import_file)
        exit(1)

    # read from formatted fixed-width file
    data = import_data(args.import_file)

    # export data to specified format
    # to make this Unix-like pipe-able
    # we just print to stdout
    print(write_data(data, args.export_format))
