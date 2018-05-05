# -*- coding: utf-8 -*-
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    
    # login information
    headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "authorization": "c3cef7c66a1843f8b3a9e6a1e3160e20", 
        "Host": "https://www.zhihu.com",
        "origin": "https://www.zhihu.com",
        "Referer": "https://www.zhihu.com/signup?next=%2F",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux86_64;rv:59.0) Gecko/20100101 Firefox/59.0"
    }
    phone = "+8618092671458"
    password = "tdp158520"
    

    def start_requests(self):
        # According to official documentation, this method must return an iterable with 
        # the first Requests to crawl for this spider.
        return [
            scrapy.Request( 
                'https://www.zhihu.com/signup?next=%2F',
                headers = self.headers,
                callback = self.cap1
            )
        ]
   
    def cap1(self, response):
        print response.text
    
    def parse(self, response):
        pass
