# -*- coding: utf-8 -*-
import scrapy


class LoginSpiderSpider(scrapy.Spider):

    name = 'login_spider'
    start_urls = ['https://www.shiyanlou.com/login']

    """
    def parse(self, response):
        """
        模拟登录的核心就在这里,scrapy会下载 start_urls 里的登录页面,将 response 传到这里,
        然后调用 FormRequest 模拟构造一个 POST 登录请求。FormRequest 继承自 Request，
        所以 Request 的参数对它适用。FormRequest 有一类方法 from_response 用于快速构建 FormRequest 对象。
        from_response 方法会从第一步返回的 response 中获取请求的 url，form 表单信息等等，
        因此只需要指定必要的表单数据和回调函数即可。
        """
        return scrapy.FormRequest.from_response(
            # 第一个参数必须传入上一步返回的 response
            response,
            # 以字典结构传入表单数据
            formdata={},
            # 指定回调函数
            callback=self.after_login
        )

    def after_login(self, response):
        """
        登录之后的代码和普通的 scrapy 爬虫一样，构造 Request，指定 callback
        """
        pass

    def parse_after_login(self, response):
        pass
    """

    def parse(self, response):
        # 获取表单的 csrf_token
        csrf_token = response.xpath('').extract_first()
        self.logger.info(csrf_token)
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                'csrf_token': csrf_token,
                # account & password
                'login': 'example@email.com'
                'password': 'password',
            },
            callback=self.after_login
        )

    def after_login(self, response):
        # 登录成功后构造一个访问自己主页的 scrapy.Request
        # 记得把 url 里的 id 换成自己的，这部分数据只能看到自己的
        return [scrapy.Request(
            url='https://www.shiyanlou.com/user/634/',
            callback=self.parse_after_login
        )]

    def parse_after_login(self, response):
        """
        解析实验次数和实验时间数据，他们都在 span.info-text 结构中。实验次数位于第 2 个，实验时间位于第 3 个。
        """
        return {
            'lab_count': response.xpath('(//span[@class="info-text"])[2]/text()').re_first('[^\d]*(\d*)[^\d*]'),
            'lab_minutes': response.xpath('(//span[@class="info-text"])[3]/text()').re_first('[^\d]*(\d*)[^\d*]')
        }
