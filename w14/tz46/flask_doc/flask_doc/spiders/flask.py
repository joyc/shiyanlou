# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from flask_doc.items import FlaskDocItem


class FlaskSpider(scrapy.spiders.CrawlSpider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = ['http://flask.pocoo.org/docs/1.0/']

    rules = (
        Rule(LinkExtractor(allow='http://flask.pocoo.org/docs/1.0/.*'), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        item = FlaskDocItem()
        item['url'] = response.url
        item['text'] = ' '.join(response.xpath('//text()').extract())
        yield item
