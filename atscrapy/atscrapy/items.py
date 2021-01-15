# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AtscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class SchemaOrgPerson(scrapy.Item):
    """
    https: // schema.org / Person
    """
    schemaorg = 'http://schema.org/Person'

    image = scrapy.Field()
    name = scrapy.Field()
    additionalName = scrapy.Field()
    worksFor = scrapy.Field()
    homeLocation = scrapy.Field()
    email = scrapy.Field()
    url = scrapy.Field()
    follows = scrapy.Field()
    twitter = scrapy.Field()
    programmingLanguage = scrapy.Field()


class GoogleSearchResult(scrapy.Item):
    link = scrapy.Field()
    data = scrapy.Field()


SCHEMA_ORG_TYPES = {
    SchemaOrgPerson.schemaorg: SchemaOrgPerson
}
