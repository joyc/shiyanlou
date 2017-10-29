# 从数据库中读取内容

## 介绍

上一个挑战中，我们实现了一个简单的资讯网站，从 JSON 文件中读取文章内容，现在我们将改造这个网站从 MySQL 数据库中读取内容。

首先使用 git clone 克隆你在 Github 上一个挑战的代码到 `/home/shiyanlou/news` 目录。

下面的 Python 代码仍然需要全部写入到 `/home/shiyanlou/news/app.py` 文件中。

如果需要安装额外的包，只需要 `sudo pip3 install 包名` 即可，不需要使用 virtualenv。此处需要安装的包有：

```
$ sudo pip3 install mysqlclient
$ sudo pip3 install Flask_SQLAlchemy

```

注意实验环境中需要手动启动 MySQL 数据库，默认的 root 用户密码为空。需要手动创建数据库，注意配置 `app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/你创建的数据库名称'`

我们介绍一个新的 Flask 的插件模块 `flask-sqlalchemy`，这个模块的作用与名字一样，就是让我们在 Flask 应用中很方便的使用 SQLAlchemy 连接数据库。

请阅读 `flask-sqlalchemy` [快速上手的教程](http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application)，不需要太深入，会根据文档使用即可。

我们需要在 Flask Web 应用中使用 `flask-sqlalchemy` 创建两个表：文章表 `class File(db.Model)` 和类别表 `class Category(db.Model)`，要求每个文章有且只属于一个类别，文章表和类别表为多对1的关系。

其中文章表包含下面的数据：

```
id：文章的ID，主键约束（db.Integer）
title: 文章名称（db.String(80)）
created_time: 文章创建时间（db.DateTime）
category_id: 文章的分类，外键约束（db.Integer, db.ForeignKey(...)）
content: 文章的内容（db.Text）

```

类别表包含下面的数据：

```
id：类别的ID，主键约束（db.Integer）
name：类别的名称（db.String(80)）

```

在 Flask 应用中需要使用 `db.create_all()` 创建数据库并使用下方代码插入测试数据（注意需要判断数据库中如果已经有了测试数据则不需要重复添加）：

```
java = Category('Java')
python = Category('Python')
file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
db.session.add(java)
db.session.add(python)
db.session.add(file1)
db.session.add(file2)
db.session.commit()

```

该网站实现后，需要包括以下路由：

```
@app.route('/')
def index():
    # 显示文章名称的列表
    # 页面中需要显示所有文章的标题（title）列表，此外每个标题都需要使用 `<a href=XXX></a>` 链接到对应的文章内容页面

@app.route('/files/<file_id>')
def file(file_id):
    # file_id 为 File 表中的文章 ID
    # 需要显示 file_id  对应的文章内容、创建时间及类别信息（需要显示类别名称）
    # 如果指定 file_id 的文章不存在，则显示 404 错误页面

```

该应用需要运行在 3000 端口，即使用实验环境中的浏览器访问 `http://localhost:3000/` 可以进入到 index 页面。

其他需求同本周学习内容的第一个挑战。

## 目标

1. 需要保持运行状态，即运行 `flask run` 之后，再点击提交结果
2. 需要保证 `http://localhost:3000/` 页面可以访问并且返回预期的页面内容，页面内容需要包含文章标题列表及文章链接地址
3. 需要保证文章内容可以通过 index 页面中的链接地址可以访问
4. 系统不会对页面布局及样式进行测试，只会检测页面内容，但希望你能够按照前面实验学习的前端知识尽可能优化页面内容展示的样式
5. 请将 `/home/shiyanlou/news` 中的代码提交到你的 Github 中，后续的挑战都会用到本次挑战实现的代码
6. 为了后续使用方便，可以不用使用 virtualenv，如果用了，也不要向 Github 提交 virtualenv 创建的虚拟环境目录

## 提示语

1. 数据库部分的实现，需要参考 MySQL 及 SQLAlchemy 实验中的内容，也需要阅读 `flask-sqlalchemy` [快速上手](http://www.pythondoc.com/flask-sqlalchemy/quickstart.html) 页面的内容

## 知识点

- MySQL 基础知识
- 关系数据库基础
- SQLAlchemy 基础知识
- `flask-sqlalchemy` 的使用方法