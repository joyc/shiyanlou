## 挑战：为文章增加标签

# 为文章增加标签

## 介绍

上一个挑战中，我们实现了一个简单的资讯网站，资讯文章的内容及分类都存入 MySQL 数据库中。

本节挑战将为每一个文章增加0到多个标签（Tag），标签与文章是多对多的关系，增加的标签存入 MongoDB。

首先使用 git clone 克隆你在 Github 上一个挑战的代码到 `/home/shiyanlou/news` 目录。

下面的 Python 代码仍然需要全部写入到 `/home/shiyanlou/news/app.py` 文件中。

如果需要安装额外的包，只需要 `sudo pip3 install 包名` 即可，不需要使用 virtualenv。此处需要安装的包有：

```
$ sudo pip3 install mysqlclient
$ sudo pip3 install Flask_SQLAlchemy

```

注意 MySQL 和 MongoDB 都需要有一些手动的初始化操作，比如创建数据库，启动服务等。

为上一节挑战中实现的文章类 `class File(db.Model)` 增加下面的两个方法和一个属性：

```
# 向文章添加标签
def add_tag(self, tag_name):
    # 为当前文章添加 tag_name 标签存入到 MongoDB
    pass

# 移除标签
def remove_tag(self, tag_name):
    # 从 MongoDB 中删除当前文章的 tag_name 标签
    pass

# 标签列表
@property
def tags(self):
    # 读取 mongodb，返回当前文章的标签列表
    pass

```

在 Flask 应用中需要使用 `db.create_all()` 创建数据库并使用下方代码插入测试数据（注意需要判断数据库及mongodb中如果已经有了测试数据则不需要重复添加）：

```
# 增加 MySQL 中的数据
java = Category('Java')
python = Category('Python')
file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
db.session.add(java)
db.session.add(python)
db.session.add(file1)
db.session.add(file2)
db.session.commit()

# 增加 MongoDB 中的数据
file1.add_tag('tech')
file1.add_tag('java')
file1.add_tag('linux')
file2.add_tag('tech')
file2.add_tag('python')

```

需要修改 index 页面显示的内容，除了文章标题及链接外还要显示文章的标签列表。

其他需求同本周学习内容的前两个挑战。

## 目标

1. 需要保持 Flask 和 MongoDB 都处于运行状态，即运行 `flask run` 之后，再点击提交结果
2. 需要保证 `http://localhost:3000/` 页面可以访问并且返回预期的页面内容，页面内容需要包含文章标题列表及文章链接地址，每个文章的标题后面都显示文章的标签列表
3. 需要保证文章内容可以通过 index 页面中的链接地址可以访问
4. 系统不会对页面布局及样式进行测试，只会检测页面内容，但希望你能够按照前面实验学习的前端知识尽可能优化页面内容展示的样式
5. 请将 `/home/shiyanlou/news` 中的代码提交到你的 Github 中，后续的挑战都会用到本次挑战实现的代码
6. 为了后续使用方便，可以不用使用 virtualenv，如果用了，也不要向 Github 提交 virtualenv 创建的虚拟环境目录

## 提示语

1. MongoDB 内的数据存储格式需要自己定义，需要保证能够通过文章 id 获取得到标签列表
2. 注意考虑如何在 add_tag 的时候避免重复添加相同的标签给同一个文章
3. 当 remove_tag 去掉文章中不存在的标签的时候，不需要报错

## 知识点

- MongoDB 的基础操作；
- `pyMongo` 的使用方法
- 面向对象中方法和属性的使用