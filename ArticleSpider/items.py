# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from scrapy.loader import ItemLoader

def remove_slash(s):
    return s.replace("/", "")


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field()
    created_date = scrapy.Field()
    url = scrapy.Field()
    url_md5 = scrapy.Field()
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()
    praise_num = scrapy.Field()
    comments_num = scrapy.Field()
    fav_num = scrapy.Field()
    tags = scrapy.Field()

class LagouJobItemLoader(ItemLoader):
    default_output_processor = TakeFirst();

class LagouJobItem(scrapy.Item):
    post_url = scrapy.Field()
    title = scrapy.Field()
    company = scrapy.Field()
    min_salary = scrapy.Field()
    city = scrapy.Field(
        input_processor = MapCompose(remove_slash)
    )
    min_work_years = scrapy.Field(
        input_processor = MapCompose(remove_slash)
    )
    degree_req = scrapy.Field(
        input_processor = MapCompose(remove_slash)
    )
    job_type = scrapy.Field(
        input_processor = MapCompose(remove_slash)
    )
    tags = scrapy.Field(
        input_processor = MapCompose(Join(",")) 
    )
    publish_time = scrapy.Field()
    advantage = scrapy.Field()
    description = scrapy.Field()
    addr = scrapy.Field()


