# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Course, engine
from scrapy.exceptions import DropItem


class ShiyanlouPipeline(object):

    def process_item(self, item, spider):
        """ parse 出来的 item 会被传入这里，这里编写的处理代码会
        作用到每一个 item 上面。这个方法必须要返回一个 item 对象。
        """
        # 提取的学习人数是字符串，把它转换成 int
        item['students'] = int(item['students'])
        # 根据 item 创建 Course Model 对象并添加到 session
        # item 可以当成字典来用，所以也可以使用字典解构, 相当于
        # Course(
        #     name=item['name'],
        #     type=item['type'],
        #     ...,
        # )

        # 保留学习人数超过 1000 的课程,过滤item结果
        if item['students'] < 1000:
            # 对于不需要的 item，raise DropItem 异常
            raise DropItem('Course students less than 1000.')
        else:
            self.session.add(Course(**item))
        return item

    def open_spider(self, spider):
        """当爬虫被开启的时候调用,创建数据库session"""
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        """当爬虫被关闭的时候调用,提交并关闭session"""
        self.session.commit()
        self.session.close()
