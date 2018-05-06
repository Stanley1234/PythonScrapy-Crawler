# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class LagouSpider(CrawlSpider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['http://www.lagou.com/']

    rules = (
        Rule(LinkExtractor(allow = r"jobs/\d+.html"), callback = "parse_job", follow = True)
    )

    def parse_job(self, response):
        item_loader = LagouJobItemLoader(item = LagouJobItem(), response = response)
        
        item_loader.add_value("post_url", response.url)

        item_loader.add_css("title", "div .job-name::attr(title)")
        item_loader.add_css("company", "div .company::text")
        item_loader.add_css("min_salary", "span.salary::text")
        item_loader.add_xpath("city", "//[@class='job_request']/p/span[2]/text()")
        item_loader.add_xpath("min_work_years", "//[@class='job-request']/p/span[3]/text()")
        item_loader.add_xpath("degree_req", "//[@class='job-request']/p/span[4]/text()")
        item_loader.add_xpath("type", "//[@class='job-request']/p/span[5]/text()")
        item_loader.add_css("tags", ".position-label li::text")
        item_loader.add_css("publish_time", ".publish_time::text")
        item_loader.add_css("advantage", ".job-advantage p::text")
        item_loader.add_css("description", ".job_bt div")  # hot about .job_bt p
        item_loader.add_css("addr", ".work_addr")


        # job_addr
        # company_name
        
        # crawl_time
        # url

        return job_item
