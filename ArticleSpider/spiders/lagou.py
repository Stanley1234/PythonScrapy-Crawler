# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ArticleSpider.items import LagouJobItem, LagouJobItemLoader

class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['http://www.lagou.com/']

    rules = (
        Rule(LinkExtractor(allow = r"zhaopin/"), follow = True),
        Rule(LinkExtractor(allow = r"jobs/\d+.html"), callback = "parse_job", follow = True),
    )
    
    # The headers Host, Referer, Cookie, User-Agent are important in this case
    # Take a look at request headers when clicking on job posts
    custom_settings = {
        "COOKIES_ENABLED": False,
        "DOWNLOAD_DELAY": 1,  # delay 1 sec before consecutive page is downloaded
        "DEFAULT_REQUEST_HEADERS" : {
            "Accept-Language": "en",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Host": "www.lagou.com",
            "Origin": "https://www.lagou.com",
            "Referer": "https://www.lagou.com",
            "Cookie": "user_trace_token=20180507050041-aa615a01-d185-4f50-a0e7-a30f58af9ce2; _ga=GA1.2.114440735.1525640479; _gid=GA1.2.550190849.1525640479; LGSID=20180507050120-a07e64af-5170-11e8-818f-5254005c3644; LGUID=20180507050120-a07e6846-5170-11e8-818f-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1525640481,1525641532; JSESSIONID=ABAAABAAAIAACBIE8D022C8D9C7DB81ED24D1C71676B0CB; LGRID=20180507054310-7859c411-5176-11e8-8fae-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1525642991; index_location_city=%E5%85%A8%E5%9B%BD; X_HTTP_TOKEN=4e04142db170d54e95d1d31d1ac60868; TG-TRACK-CODE=index_hotjob; _gat=1",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64;rv:59.0) Gecko/20100101 Firefox/59.0"
        }
    }

    def parse_job(self, response):
        item_loader = LagouJobItemLoader(item = LagouJobItem(), response = response)
        
        item_loader.add_value("post_url", response.url)
        item_loader.add_css("title", "div .job-name::attr(title)")
        item_loader.add_css("company", "div .company::text")
        item_loader.add_css("min_salary", "span.salary::text")
        item_loader.add_xpath("city", "//*[@class='job_request']/p/span[2]/text()")
        item_loader.add_xpath("min_work_years", "//*[@class='job-request']/p/span[3]/text()")
        item_loader.add_xpath("degree_req", "//*[@class='job-request']/p/span[4]/text()")
        item_loader.add_xpath("job_type", "//*[@class='job-request']/p/span[5]/text()")
        item_loader.add_css("tags", ".position-label li::text")
        item_loader.add_css("publish_time", ".publish_time::text")
        item_loader.add_css("advantage", ".job-advantage p::text")
        item_loader.add_css("description", ".job_bt div")  # hot about .job_bt p
        item_loader.add_css("addr", ".work_addr")

        job_item = item_loader.load_item()
        return job_item
