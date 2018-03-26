# -*- coding: utf-8 -*-
import scrapy


class GithubSpider(scrapy.Spider):
    """ 所有 scrpy 爬虫需要写一个 Spider 类，这个类要继承 scrapy.Spider 类。
    在这个类中定义要请求的网站和链接、如何从返回的网页提取数据等等。
    """
    # 爬虫标识符号，在 scrapy 项目中可能会有多个爬虫，name 用于标识每个爬虫，不能相同
    name = 'shiyanlou-github'

    @property
    def start_urls(self):
        """ start_urls 需要返回一个可迭代对象，所以，你可以把它写成一个列表、元组或者生成器，这里用的是元组
        """
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1, 5))

    def parse(self, response):
        for repository in response.css('li.public'):
            yield {
                'name': repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first("\n\s*(.*)"),
                'update_time': repository.xpath('.//relative-time/@datetime').extract_first()
            }