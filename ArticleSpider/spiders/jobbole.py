# -*- coding: utf-8 -*-

import scrapy
import re

from scrapy.http import Request
from urlparse import urljoin
from ArticleSpider.items import JobBoleArticleItem

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts']

    
    def parse(self, response):
        # parse all posts on the current page
        allposts = response.xpath("//div[@class='post floated-thumb']//div[@class='post-thumb']")
        for post in allposts:
            post_url = post.xpath("./a/@href").extract_first()
            front_img_url = post.xpath("./a/img/@src").extract_first()
            
            # urljoin(base, url)
            yield Request(url = urljoin(response.url, post_url),
                          meta = {"front_image_url": front_img_url},
                          callback = self.parse_page) 

        # go to next page
        next_url = response.xpath("//a[@class='next page-numbers']/@href").extract_first()
        if next_url:
            yield Request(url = urljoin(response.url, next_url), callback = self.parse)


    def parse_page(self, response):
        
        article_item = JobBoleArticleItem() 
        
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first()
        # take the first text node
        created_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract_first()  
        praise_num = response.xpath('//span[contains(@class, "vote-post-up")]/h10/text()').extract_first()
        
        fav_num = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract_first()
        fav_match = re.match(".*?(\d+).*", fav_num)
        if fav_match:
            fav_num = fav_match.group(1)
        else:
            fav_num = "0"

        comments_num = response.xpath("//span[contains(@class, 'btn-bluet-bigger')]/text()").extract_first()
        comments_match = re.match(".*?(\d+)(.*)", comments_num)
        if comments_match:
            comments_num = comments_match.group(1)
        else:
            comments_num = "0"
        
        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith(u"评论")]
        tags = ",".join(tag_list)

        
        article_item["url"] = response.url
        article_item["title"] = title
        article_item["created_date"] = created_date
        article_item["praise_num"] = praise_num
        article_item["fav_num"] = fav_num
        article_item["comments_num"] = comments_num
        article_item["tags"] = tags
       
        article_item["front_image_url"] = [response.meta["front_image_url"]]
        # pipeline the article item
        yield article_item 
        '''
        print "title:" + title
        print "date:" + re.sub("\s+", "", created_date)
        print "praise:" + praise_num
        print "fav:" + fav_num
        print "comments:" + comments_num
        print "tags:"  + tags
        '''
