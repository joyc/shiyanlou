#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/11/3 12:05
# @Author  : Hython.com
# @File    : scrapysyl.py
import scrapy


class ShiyanlouCourseSpider(scrapy.Spider):
    """所有爬虫类需要写Spider类并继承scrapy.Spider类"""
    # 命名爬虫标识符
    name = 'shiyanlou-course'

    # def start_requests(self):
    # 	url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
    # 	urls = (url_tmpl.format(i) for i in range(1, 24))
    # 	for url in urls:
    # 		yield scrapy.Request(url=url, callback=self.parse)
    @property
    def start_urls(self):
        """start_urls 需要一个可迭代对象：列表，集合，生成器"""
        url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        return (url_tmpl.format(i) for i in range(1, 24))

    def parse(self, response):
        """这个方法作为 `scrapy.Request` 的 callback，在里面编写提取数据的代码。
        scrapy 中的下载器会下载 `start_reqeusts` 中定义的每个 `Request`
        并且结果封装为一个 response 对象传入这个方法。"""
        for course in response.css('div.course-body'):
            yield {
                'name': course.css('div.course-name::text').extract_first(),
                'description': course.css('div.course-desc::text').extract_first(),
                'type': course.css('div.course-footer span.pull-right::text').extract_first(default='free'),
                'students': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d*)[^\d]*')
            }