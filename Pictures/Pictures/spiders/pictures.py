# -*- coding: utf-8 -*-
import scrapy


class PicturesSpider(scrapy.Spider):
    name = "pictures"
    allowed_domains = ["pic.com"]
    start_urls = ['http://pic.com/']

    def parse(self, response):
        pass
