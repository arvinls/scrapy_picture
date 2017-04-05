# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request

class PicturesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for image_url in item['image_url']:
            #这里不仅要吧image_url传过去，还要将item传过去，
            #因为后面图片要用到items里面的名字
            yield Request(image_url, meta={'item': item})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results in ok]
        if not image_paths:
            raise DropItem('the image is wrong %s' % image_paths)

    #要想给图片改名字，就要覆盖file_path这个函数
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        #提取文件名
        image_guid = request.url.split('/')[-1]
        #拼接文件名
        filename = u'full/{0[title]}/{1}'.format(item, image_guid)
        return filename
