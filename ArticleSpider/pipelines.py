# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter

class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item

class ArticleImagePipeline(ImagesPipeline):
    # rewrite the method to know the stored path of an image
    def item_completed(self, results, item, info):
        # there is only one iteration in this program
        for ok, value in results:
            image_file_path = value["path"]
        item["front_image_path"] = image_file_path
        return item


class JsonExporterPipeline(object):
    def __init__(self):
        self.file = open("articleexport.json", "wb")
        self.exporter = JsonItemExporter(self.file, encoding = "utf-8", ensure_ascii = False)
        self.exporter.start_exporting()
    
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item
    
    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


'''
Scrapy provides json exporter. We can directly use it
instead of creating a customized one.
'''
class JsonWithEncodingPipeline(object):
    # save the data to local in json format
    def __init__(self):
        self.file = codecs.open("article.json", "w", encoding="utf-8")
    
    def process_item(self, item, spider):
        # now item is of type JobBoleArticleItem 
        # convert item to dict
        item_dict = dict(item)
        # convert dict item to a json object
        # some characters are unicode characters
        item_json = json.dumps(item_dict, ensure_ascii = False)
        self.file.write(item_json + "\n")
        return item
    
    def spider_closed(self, spider):
        # release file handler
        self.file.close()

