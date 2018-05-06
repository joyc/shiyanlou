import scrapy


class GithubSylSpider(scrapy.Spider):

    name = "shiyanlou-repository"

    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1, 4))

    def parse(self, response):
        for repo in response.css('li.public'):
            yield {
                'name': repo.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first('\n\s*(.*)'),
                'description': repo.xpath('.//p[@itemprop="description"]/text()').re_first('\n\s*(.*)\s'),
                'update_time': repo.xpath('.//relative-time/@datetime').extract_first()
            }

