# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.item import MultipageCourseItem


class MultipageSpider(scrapy.Spider):
    name = 'multipage'
    start_urls = ['https://www.shiyanlou.com/courses/']

    def parse(self, response):
        for course in response.css('a.course-box'):
            item = MultipageCourseItem()
            # 解析课程名称
            item['name'] = course.xpath('.//div[@class="course-name"]/text()').extract_first()
            # 解析课程图片
            item['image'] = course.xpath('.//img/@src').extract_first()
            # 构造课程详情页面的链接，爬取到的链接是相对链接，调用 urljoin 方法构造全链接
            course_url = response.urljoin(course.xpath('@href').extract_first())
            # 构造到课程详情页的请求，指定回调函数
            request = scrapy.Request(course_url, callback=self.parse_author)
            # 将未完成的 item 通过 meta 传入 parse_author
            request.meta['item'] = item
            yield request

    def parse_author(self, response):
        # 获取未完成的 item
        item = response.meta['item']
        # 解析课程作者
        item['author'] = response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
        # item 构造完成，生成
        yield item
