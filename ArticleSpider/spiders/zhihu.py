# -*- coding: utf-8 -*-
import scrapy
import json

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    #start_urls = ['http://www.zhihu.com/']
    
    # login information
    # header information must be ensured valid
    headers = {
        "Accept-Language":"en-US,en;q=0.5",
        "authorization": "oauth c3cef7c66a1843f8b3a9e6a1e3160e20", 
        "Host": "www.zhihu.com",
        "origin": "https://www.zhihu.com",
        "Referer": "https://www.zhihu.com/signup?next=%2F",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux86_64;rv:59.0) Gecko/20100101 Firefox/59.0"
    }
    

    def start_requests(self):
        # According to official documentation, this method must return an iterable with 
        # the first Requests to crawl for this spider.
        return [
            scrapy.Request( 
                url = 'https://www.zhihu.com/signup?next=%2F',
                headers = self.headers,
                callback = self.cap1,
            )
        ]
   
    def cap1(self, response):
        return [
            scrapy.Request(
                url = "https://www.zhihu.com/api/v3/oauth/captcha?lang=en",
                headers = self.headers,
                callback = self.cap2
            )        
        ]

    def cap2(self, response):
        return [
            scrapy.Request(
                url = "https://www.zhihu.com/api/v3/oauth/captcha?lang=en",
                headers = self.headers,
                callback = self.login,
                dont_filter = True
            )
        ]
    
    def login(self, response):
        login


    def parse(self, response):
        pass
