#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ooshiroharuya
@software: PyCharm
@file: Test02.py
@time: 2022/3/21 22:59
"""

from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

