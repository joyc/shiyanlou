#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/25/0025 23:56
# @Author  : Hython.com
# @File    : rest.py
"""rmon.common.rest
"""


class RestException(Exception):
    """异常基类"""

    def __init__(self, code, message):
        """初始化异常
        Args:
            code(int): http状态码
            message(str): 错误信息
        """
        self.code = code
        self.message = message
        super(RestException, self).__init__()
