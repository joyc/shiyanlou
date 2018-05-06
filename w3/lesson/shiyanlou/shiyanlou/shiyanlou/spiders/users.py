# -*- coding: utf-8 -*-
import scrapy
import json
# import requests
from datetime import datetime, timedelta
from shiyanlou.items import UserItem


class UsersSpider(scrapy.Spider):
    name = 'users'
    # allowed_domains = ['shiyanlou.com']
    # start_urls = ['http://shiyanlou.com/']

    @property
    def start_urls(self):
        """
        注册用户数目前大约50几万，这里取 id 在 524,700~525,500 之间的新用户，
        每间隔 20 取一个，最后大概爬取 40 个用户的数据
        """
        return ('https://www.shiyanlou.com/user/{}/'.format(i) for i in range(525500, 524700, -20))

    def parse(self, response):
        yield UserItem({
            'name': response.css('span.username::text').extract_first(),
            'type': response.css('a.member-icon img.user-icon::attr(title)').extract_first(default='普通用户'),
            'status': response.xpath('//div[@class="userinfo-banner-status"]/span[1]/text()').extract_first(),
            'job': response.xpath('//div[@class="userinfo-banner-status"]/span[2]/text()').extract_first(),
            'school': response.xpath('//div[@class="userinfo-banner-status"]/a/text()').extract_first(),
            'join_date': response.css('span.join-date::text').extract_first(),
            'level': response.css('span.user-level::text').extract_first(),
            'learn_courses_num': response.css('span.latest-learn-num::text').extract_first()
        })
