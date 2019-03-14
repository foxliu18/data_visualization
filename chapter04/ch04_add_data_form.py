# -*- coding: utf-8 -*-
# @Time    : 3/14/19
# @Author  : lkx-rog
# @Project : data_visualization
# @File    : ch04_add_data_form
# @Software: PyCharm
import matplotlib.pylab as plt
import numpy as np


def main():
    plt.figure()
    ax = plt.gca()
    y = np.random.randn(9)

    col_label = ['col1', 'col2', 'col3']
    row_label = ['row1', 'row2', 'row3']
    table_value = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
    row_color = ['red', 'gold', 'green']
    my_table = plt.table(cellText=table_value,
                         colWidths=[0.1] * 3,
                         rowLabels=row_label,
                         colLabels=col_label,
                         rowColours=row_color,
                         loc='upper right')
    plt.plot(y)
    plt.show()


if __name__ == '__main__':
    main()
