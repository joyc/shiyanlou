#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/10/19 0:00
# @Author  : Hython.com
# @File    : ptest.py
import sys

list = sys.argv[1:]
print(list)
for i in list:
    print(i.split(":")[0])
    print(i.split(":")[1])
    # for j in (i[0].split(":")):
    #     print(j)