#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/5 19:39
# @Author  : Hython.com
# @File    : models.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date


engine = create_engine('mysql+mysqldb://root:password@localhost:3306/shiyanlou?charset=utf8')
Base = declarative_base()


class Course(Base):
    """建表"""
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    description = Column(String(1024))
    type = Column(String(64), index=True)
    students = Column(Integer)


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    type = Column(String(64))
    status = Column(String(64), index=True)
    school = Column(String(64))
    job = Column(String(64))
    level = Column(Integer, index=True)
    join_date = Column(Date)
    learn_courses_num = Column(Integer)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
