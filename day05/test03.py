#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: YvesHu
@time: 2022/3/20 23:24
"""

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello, world")
    elif len(args) == 2:
        print("Hello %s!") % args[1]
    else:
        print("too much arguments!")

"""
由于每个PYTHON模块都包含内置的变量__name__，当运行模块被执行的时候，
__name__等于文件名（包含了后缀.py)。如果import到其他模块中，则__name__
等于模块名称（不包含后缀.py)。而__main__等于当前执行文件的名称（包含了
后缀.py)。所以当模块被直接执行时，__name__=='__main__'结果为真；
而当模块被import到其他模块中时，__name__=='__main__'结果为假，就是
不调用对应的方法
"""
if __name__ == '__main__':
    test()