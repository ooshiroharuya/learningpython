#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ooshiroharuya
@software: PyCharm
@file: Student.py
@time: 2022/3/21 12:46 上午
"""

class Student(object):

    def __init__(self, name, score, gender):
        self.name = name
        self.score = score
        self.__gender = gender

    def print_score(self):
        print("%s: %s" % (self.name, self.score))

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):

        if not isinstance(gender, str):
            raise TypeError("请输入字符串")

        self.__gender = gender
        return
