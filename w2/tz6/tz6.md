# 一个简单的资讯网站

## 介绍

使用所学的 Flask 开发一个简单的资讯类网站应用。该网站可以展示文章列表，以及每个文章里的详细内容。

首先，打开 Xfce 终端，执行下面的命令，下载网站所需的文章数据：

```
$ cd /home/shiyanlou
$ mkdir files
$ cd files
$ wget http://labfile.oss.aliyuncs.com/courses/923/week2/helloshiyanlou.json
$ wget http://labfile.oss.aliyuncs.com/courses/923/week2/helloworld.json

```

这两个 json 文件是我们的咨询网站将使用的两篇文章数据。内部的格式为 json，包含下面的数据项：

```
title: 文章名称（字符串）
created_time: 文章创建时间（字符串）
content: 文章的内容（字符串）

```

创建代码目录结构：

```
$ cd /home/shiyanlou
$ mkdir news
$ cd news
$ mkdir templates
$ touch app.py templates/404.html templates/base.html templates/index.html templates/file.html

```

该网站实现后，需要包括以下路由，所有 Python 代码写入 `/home/shiyanlou/news/app.py` 中：

```
@app.route('/')
def index():
    # 显示文章名称的列表
    # 页面中需要显示 `/home/shiyanlou/files/` 目录下所有 json 文件中的 `title` 信息列表

@app.route('/files/<filename>')
def file(filename):
    # 读取并显示 filename.json 中的文章内容
    # 例如 filename='helloshiyanlou' 的时候显示 helloshiyanlou.json 中的内容
    # 如果 filename 不存在，则显示包含字符串 `shiyanlou 404` 404 错误页面

```

该应用需要运行在 3000 端口，即使用实验环境中的浏览器访问 `http://localhost:3000/` 可以进入到 index 页面。

另外，需要自定义 404 NOTFOUND 页面，如果访问的页面不存在，则需要返回的页面中包含字符串 `shiyanlou 404`。

## 目标

1. 需要保持运行状态，即运行 `flask run` 之后，再点击提交结果
2. 需要保证 `http://localhost:3000/` 页面可以访问并且返回预期的页面内容，页面内容需要包含文章列表
3. 需要保证 `http://localhost:3000/files/helloshiyanlou` 可以访问到 `/home/shiyanlou/files/helloshiyanlou.json` 文件中的内容
4. 需要保证 `http://localhost:3000/files/helloworld` 可以访问到 `/home/shiyanlou/files/helloworld.json` 文件中的内容
5. 系统不会对页面布局及样式进行测试，只会检测页面内容，但希望你能够按照前面实验学习的前端知识尽可能优化页面内容展示的样式
6. 代码必须放在 `/home/shiyanlou/news` 目录下，Python 代码必须放在 `app.py` 文件中
7. 请将 `/home/shiyanlou/news` 中的代码提交到你的 Github 中，后续的挑战都会用到本次挑战实现的代码
8. 为了后续使用方便，可以不用使用 virtualenv，如果用了，也不要向 Github 提交 virtualenv 创建的虚拟环境目录

## 提示语

1. 修改 Flask 运行使用 3000 端口号可以使用 `flask run` 中的参数，请查阅 Flask 文档解决
2. index 路由实现中，需要使用 `os` 模块读取目标目录 `/home/shiyanlou/files` 下的 json 文件列表，然后将 json 文件使用上周学习的 json 序列化方式转成 Python 字典，最后使用 `render_templates` 函数使用字典对象生成页面。
3. file 路由实现中，需要使用 `os.path` 模块查看目标目录 `/home/shiyanlou/files` 是否有 `filename.json` 文件，如果不存在则返回包含字符串 `shiyanlou 404` 的 404 页面，如果有则使用 json 序列化方式提取内容并使用 `render_templates` 展示到页面上。
4. 注意需要按照先前学的自定义 Flask 404 页面

## 知识点

- Flask 基本使用
- Flask 自定义错误页面
- 注册路由
- 模板渲染
- Jinja 语法
- Jinja 继承
- HTML 语法
- CSS 语法
- JSON 序列化
- os 模块