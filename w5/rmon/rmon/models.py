""" rmon.model

该模块实现了所有的 model 类以及相应的序列化类
"""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from redis import StrictRedis, RedisError
from .common.rest import RestException

db = SQLAlchemy()


class Server(db.Model):
    """Redis服务器模型
    """

    __tablename__ = 'redis_server'

    id = db.Column(db.Integer, primary_key=True)
    # unique = True 设置不能有同名的服务器
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(512))
    host = db.Column(db.String(15))
    port = db.Column(db.Integer, default=6379)
    password = db.Column(db.String())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 用于打印时看到server类实例的名称
    def __repr__(self):
        return '<Server(name=%s)>' % self.name

    @property
    def redis(self):
        return StrictRedis(host=self.host, port=self.port, password=self.password)

    def save(self):
        """将Server实例保存到数据库中
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """将Server实例从数据库中删除
        """
        db.session.delete(self)
        db.session.commit()

    def ping(self):
        """检查 Redis 服务器是否可以访问
        """
        try:
            return self.redis.ping()
        except RedisError:
            raise RestException(400, 'redis server %s can not connected' % self.host)

    def get_metrics(self):
        """获取Redis服务器监控信息，通过Redis服务器指令INFO
        返回监控信息，参考 https://redis.io/commands/INFO
        """
        try:
            return self.redis.info()
        except RedisError:
            raise RestException(400, 'redis server %s can not connected' % self.host)
