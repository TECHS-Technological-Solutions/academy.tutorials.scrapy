import re
import scrapy
from atscrapy import resources, items


class GithubSearchSpider(scrapy.Spider):
    name = 'github_search_spider'
    allowed_domains = ['github.com']

    def __init__(self, **kwargs):
        self.query = kwargs
        self.resource = resources.GitHubWebResources()
        super().__init__(**kwargs)

    def start_requests(self):
        while True:
            url = self.resource.make(self.query)
            if self.resource.page_limit_reached:
                break
            yield scrapy.Request(url)

    def parse(self, response):
        for user_list_item in response.css('#user_search_results .user-list .user-list-item a'):
            attrib = user_list_item.attrib
            if attrib.get('data-hovercard-type', None) == 'user':
                yield response.follow('https://github.com{0}'.format(attrib['href']), self.parse_user)

    def parse_user(self, response):
        """
        Github is using https://schema.org/, and this contain a resources
        to describe a web content so it is easy to scrap for search engines.
        :param response:
        :return:
        """
        for itemscope in response.xpath('.//*[@itemscope]'):
            itemtype = itemscope.xpath('@itemtype').extract()[0]
            obj = items.SCHEMA_ORG_TYPES[itemtype]()
            for property in itemscope.xpath('.//*[@itemprop]'):
                itempropk = property.xpath('@itemprop').extract()[0]
                itempropv = property.xpath('string(.)').extract()
                if itempropk == 'name':
                    obj[itempropk] = ' '.join(itempropv)
                else:
                    obj[itempropk] = re.sub(r"[\n\t\s]*", "", ' '.join(itempropv))
            # not sure why programmingLanguage was not discovered ? possibly wrong xpath syntax ?
            # or it doesn't belong to any itemtype.
            obj['programmingLanguage'] = list(
                set(response.xpath(".//*[@itemprop='programmingLanguage']")
                    .xpath('string(.)').extract())
            )
            yield obj
