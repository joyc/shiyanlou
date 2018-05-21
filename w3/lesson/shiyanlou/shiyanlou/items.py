# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class CourseImageItem(scrapy.Item):
    # 要下载的图片 url 列表
    image_urls = scrapy.Field()
    # 下载的图片会先放着这里
    images = scrapy.Field()


class CourseItem(scrapy.Item):
    """
    定义 Item 需要继承 scrapy.Item 类，将每个要爬取的数据声明为 scrapy.Field()。
    下面定义了每个课程要爬取的 4 个数据。
    """
    # define the fields for your item here like:
    name = scrapy.Field()
    description = scrapy.Field()
    type = scrapy.Field()
    students = scrapy.Field()


class UserItem(scrapy.Item):
    name = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()
    job = scrapy.Field()
    school = scrapy.Field()
    level = scrapy.Field()
    join_date = scrapy.Field()
    learn_courses_num = scrapy.Field()


class MultipageCourseItem(scrapy.Item):
    name = scrapy.Field()
    image = scrapy.Field()
    author = scrapy.Field()
