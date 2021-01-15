import scrapy
import json
from atscrapy import resources, items


class GoogleSearchSpider(scrapy.Spider):
    name = 'google_search_spider'
    allowed_domains = ['google.com']
    base_url = 'https://google.com/search?q={q}'

    def __init__(self, **kwargs):
        self.query = kwargs
        super().__init__(**kwargs)

    def start_requests(self):
        with open('./GithubSearchSpider.json') as file:
            data = json.loads(file.read())
            for record in data:
                resource = resources.GoogleSearchWebResources(text=record['name'])
                url = resource.make(self.query)
                yield scrapy.Request(url, meta={'data': record})

    def parse(self, response):
        """
        try to get linkedin page
        :param response:
        :return:
        """
        for a in response.xpath(".//a[@href][re:test(., '.*linkedin.com.*')]"):
            href = a.attrib['href']
            obj = items.GoogleSearchResult()
            linkedin = None
            try:
                linkedin = href.split('/url?q=')[1].split('&')[0]
            except (Exception,) as err:
                pass
            obj['link'] = linkedin
            obj['data'] = response.meta['data']
            yield obj
