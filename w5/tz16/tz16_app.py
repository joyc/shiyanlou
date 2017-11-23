""" app

该模块主要实现了 app 创建函数
挑战16从json读取配置信息并保存至config属性
"""
import os
import json
from flask import Flask


def create_app():
    """ 创建并初始化 Flask app
    Returns:
        app (object): Flask App 实例
    """

    app = Flask('rmon')

    # 获取 json 配置文件名称
    file = os.environ.get('RMON_CONFIG')

    # TODO 从 json 文件中读取配置项并将每一项配置写入 app.config 中
    content = ''
    try:
        with open(file) as f:
            for l in f:
                l = l.strip()
                if l.startswith('#'):
                    continue
                else:
                    continue += l
    except IOError:
        return app

    try:
        data = json.loads(content)
    except:
        return app

    for key in data:
        app.config[key.upper()] = data.get(key)
    return app
