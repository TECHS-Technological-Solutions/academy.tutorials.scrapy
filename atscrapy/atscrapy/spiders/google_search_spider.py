import scrapy


class GoogleSearchSpider(scrapy.Spider):
    name = 'google_search_spider'
    allowed_domains = ['google.com']
    base_url = 'https://google.com/search?q={q}'

    def __init__(self, q=None, **kwargs):
        self.q = q
        super().__init__(**kwargs)

    def start_requests(self):
        yield scrapy.Request(self.base_url.format(q=self.q))

    def parse(self, response):
        pass
