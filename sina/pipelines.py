# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SinaPipeline(object):
    def __init__(self):
        self.file = open('items.txt', 'w')

    def process_item(self, item, spider):
        print >> self.file, item['link'].encode('utf-8')
        print >> self.file, item['title'].encode('utf-8')
        print >> self.file, item['pub_date'].encode('utf-8')
        print >> self.file, item['body'].encode('utf-8')
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.file.close()
