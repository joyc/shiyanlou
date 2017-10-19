#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/19 0:00
# @Author  : Hython.com
# @File    : ptest.py
import sys


# def check_int(*list):
#     income = []
#     for i in list:
#         try:
#             income.append(int(i.split(":")[1]))
#         except ValueError:
#             print("Parameter Error")
#     print(income)
#     return income


list = sys.argv[1:]
print(list)
income = []
for i in list:
    try:
        income.append(int(i.split(":")[1]))
    except ValueError:
        print("Parameter Error")
print(income)