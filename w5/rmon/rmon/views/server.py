#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/27/0027 20:20
# @Author  : Hython.com
# @File    : server.py
""" rmon.views.host

实现了所有的视图控制器
"""
from flask import request, g

from rmon.common.rest import RestView
from rmon.common.decorators import ObjectMustBeExist
from rmon.models import Server, ServerSchema


class ServerList(RestView):
    """Redis 服务器列表"""
    def get(self):
        """获取Redis服务器列表"""
        servers = Server.query.all()
        return ServerSchema().dump(servers, many=True).data

    def post(self):
        """创建Redis实例"""
        data = request.get_json()
        server, errors = ServerSchema().load(data)
        if errors:
            return errors, 400
        server.ping()
        server.save()
        return {'ok': True}, 201


class ServerDetail(RestView):
    """Redis serer list"""
    method_decorators = (ObjectMustBeExist(Server), )

    def get(self, object_id):
        """获取服务器详情"""
        data, _ = ServerSchema().dump(g.instance)
        return data

    def put(self, object_id):
        """更新服务器"""
        schema = ServerSchema(context={'instance': g.instance})
        data = request.get_json()
        server, errors = schema.load(data, partial=True)
        if errors:
            return errors, 400
        server.save()
        return {'ok': True}

    def delete(self, object_id):
        """删除服务器"""
        g.instance.delete()
        return {'ok': True}, 204
