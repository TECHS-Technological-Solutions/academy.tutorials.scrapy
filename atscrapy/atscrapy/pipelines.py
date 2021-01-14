# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter
from atscrapy import items


class AtscrapyPipeline:

    def __init__(self):
        self.file = None
        self.resources = []

    def open_spider(self, spider):
        fname = '{0}.json'.format(spider.__class__.__name__)
        self.file = open(fname, 'w+')

    def close_spider(self, spider):
        self.file.write(json.dumps(self.resources))
        self.file.close()

    def process_item(self, item, spider):
        if isinstance(item, items.SchemaOrgPerson):
            self.resources.append(item.__dict__['_values'])

        return item
