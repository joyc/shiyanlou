#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2017/10/28 1:23
# @Author  : Hython.com
# @File    : app.py.py

from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
	filepath = '../files/'
	os.chdir(filepath)
	titles = []
	for file in os.listdir():
		if file.endswith('.json'):
			with open(file, 'r') as f:
				contents = json.loads(f.read())
				title = contents['title']
				titles.append(title)
	return 'article title : {}'.format([t for t in titles])



@app.route('/files/<filename>')
def file(filename):
	filepath = '../files/'
	with open(filepath + filename + '.json', 'r') as f:
		contents = json.loads(f.read())
		content = contents['content']
	return content

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

if __name__ == '__main__':
	app.run(debug=True)
