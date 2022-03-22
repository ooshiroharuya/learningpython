#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ooshiroharuya
@software: PyCharm
@file: TestDict.py
@time: 2022/3/21 23:23
"""
import unittest

from Dict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
