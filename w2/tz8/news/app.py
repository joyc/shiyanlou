#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2017/10/28 1:23
# @Author  : Hython.com
# @File    : app.py

from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
filepath = '../files/'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/shiyanlou'
db = SQLAlchemy(app)


class File(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
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
    __tablename__ = 'categories'

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


@app.route('/')
def index():
    file_list = File.query.all()
    return render_template('index.html', filelist=file_list)


@app.route('/files/<int:file_id>')
def file(file_id):
    file_item = File.query.get_or_404(file_id)
    return render_template('file.html', fileitem=file_item)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(port=3000,debug=True)
