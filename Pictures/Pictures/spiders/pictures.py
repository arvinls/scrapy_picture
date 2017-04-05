# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy.selector import Selector 
from scrapy.http import Request

from Pictures.items import PicturesItem


class PicturesSpider(Spider):
    name = "pictures"

    #allowed_domains = ["pic.com"]
    
    start_urls = []

    def start_requests(self):
        #the url cl
        url_pre = 'xxxxxxx'
        #the page_number which we want to get
        for num in xrange(1, 3):
            url_end = str(num)
            url = url_pre + url_end
            print url
            self.start_urls.append(url)
        for url in self.start_urls:
            yield self.make_requests_from_url(url)


    def parse(self, response):
        sel = Selector(response)
        item = PicturesItem()
        url_pre = 'xxxxxxx'
        url_next = sel.xpath('//td[@style="padding-left:8px"]/h3/a/@href').extract()
        for url_n in url_next:
            url = url_pre + url_n

            yield Request(url, callback = self.parse_item)
    def parse_item(self, response):
        sel = Selector(response)
        item = PicturesItem()
        img_url = sel.xpath('//div[@class="tpc_content do_not_catch"]/input/@src').extract()
        
        #这里extract出来的是一个list
        title = sel.xpath('//td[@class="h"]/text()').extract()[1]

        item['image_url'] = img_url
        item['title'] = title
        print img_url, title ,'/n'
        return item

