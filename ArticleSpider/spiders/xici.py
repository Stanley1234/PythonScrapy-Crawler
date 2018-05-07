# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ArticleSpider.items import XiciItem, XiciItemLoader

class XiciSpider(CrawlSpider):
    name = 'xici'
    allowed_domains = ['www.xicidaili.com']
    start_urls = ['http://www.xicidaili.com/nn/']
    
    custom_settings = {
        "DOWNLOAD_DELAY": 1,
        "DEFAULT_REQUEST_HEADERS": {
            "Cookie": "_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJTA1NWZhNjNhMzIyNzI4NGQ5YWFkN2ExYWY5NDZkMmQxBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXl0aGw3SCtpUkhSSkpuakROS1AyamltcTJMaitnejJicGNWd3JtNDVaRW89BjsARg%3D%3D--24e4979aadf77efb81feafb204cba7b72dd672cb; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1525647422; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1525647422",
            "Connection": "keep-alive",
            "Host": "www.xicidaili.com",
            "Referer": "http://www.xicidaili.com/nn/",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"

        }
    }

    rules = (
        Rule(LinkExtractor(allow=r'/nn/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item_loader = XiciItemLoader(item = XiciItem(), response = response)
        
        item_loader.add_css("country", "td.country img::attr(src)")
        item_loader.add_xpath("ipaddr", "//tr/td[2]/text()")
        item_loader.add_xpath("port", "//tr/td[3]/text()")
        item = item_loader.load_item()
        return item
