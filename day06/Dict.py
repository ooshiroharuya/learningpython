#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: ooshiroharuya
@software: PyCharm
@file: Dict.py
@time: 2022/3/21 23:15
"""
import logging


class Dict(dict):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            logging.ERROR(f"THere is no key: {key}")
            raise AttributeError(r"'Dict' object has no attribute '$s'" % key)

    def __setattr__(self, key, value):
        self[key] = value