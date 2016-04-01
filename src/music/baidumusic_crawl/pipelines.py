# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exporters import JsonItemExporter
from scrapy.utils.serialize import ScrapyJSONEncoder


import json
import codecs

class BaidumusicPipeline(object):
    """write item into json file"""

    def __init__(self):
        self.file = codecs.open('artist_pipeline.json', 'w', encoding='utf-8')
        #self.file = open('artist_pipeline.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "," +"\n"
        #line = line.encode("utf-8")
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


class BaidumusicJsonItemExporter(JsonItemExporter):
    def __init__(self, file, **kwargs):
        super(BaidumusicJsonItemExporter, self).__init__(file, **kwargs)
        self.encoder = ScrapyJSONEncoder(ensure_ascii=False)

