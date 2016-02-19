# -*- coding: utf-8 -*-

from functools import reduce


def str2float(s):
    nums = map(lambda x: {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': -1}[x],
               s)
    point = 0

    def fn(x, y):
        nonlocal point
        if y == -1:
            point = 1
            return x
        if point == 0:
            return x * 10 + y
        else:
            point *= 10
            return x + y / point

    return reduce(fn, nums, 0.0)


print('str2float(\'123.456\') =', str2float('123.456'))
print('str2float(\'123.456\') =', str2float('123.456'))
