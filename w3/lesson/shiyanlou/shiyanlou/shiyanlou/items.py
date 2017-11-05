# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CourseItem(scrapy.Item):
    """定义 Item 非常简单，只需要继承 scrapy.Item 类，将每个要爬取
    的数据声明为 scrapy.Field()。下面中上一节中每个课程要爬取的 4
    个数据。
    """
    # define the fields for your item here like:
    name = scrapy.Field()
    description = scrapy.Field()
    type = scrapy.Field()
    students = scrapy.Field()
