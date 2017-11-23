""" rmon.model

该模块实现了所有的 model 类以及相应的序列化类
"""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

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
