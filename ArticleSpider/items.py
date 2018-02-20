# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field()
    created_date = scrapy.Field()
    url = scrapy.Field()
    front_image_url = scrapy.Field()
    praise_num = scrapy.Field()
    comments_num = scrapy.Field()
    fav_num = scrapy.Field()
    tags = scrapy.Field()

