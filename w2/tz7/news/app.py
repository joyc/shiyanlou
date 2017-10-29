#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2017/10/28 1:23
# @Author  : Hython.com
# @File    : app.py

import os
import json
from datetime import datetime
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
filepath = '../files/'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/shiyanlou'
db = SQLAlchemy(app)


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    category = db.relationship('Category',
        backref=db.backref('articles', lazy='dynamic'))

    def __init__(self, title, created_time, category, content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content

    def __repr__(self):
        return '<File %r>' % self.content


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name


# db.create_all()

# java = Category('Java')
# python = Category('Python')
# file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
# file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
# db.session.add(java)
# db.session.add(python)
# db.session.add(file1)
# db.session.add(file2)
# db.session.commit()

file_list = File.query.all()

@app.route('/')
def index():
    return render_template('index.html', filelist=file_list)


@app.route('/files/<file_id>')
def file(filename):
    try:
        with open(filepath + filename + '.json', 'r') as f:
            contents = json.loads(f.read())
            content = contents['content']
        return content
    except IOError:
        return not_found


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(port=3000,debug=True)
