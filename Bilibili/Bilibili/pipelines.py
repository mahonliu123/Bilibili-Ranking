# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class BilibiliPipeline(object):
    def __init__(self):
        self.MONGO_URL = 'localhost'
        self.MONGO_DB = 'BILIBILI'
        self.MONGO_TABLE = 'bilibili'

    def process_item(self, item, spider):
        d_item = dict(item)
        client = pymongo.MongoClient(self.MONGO_URL, connect=False)
        db = client[self.MONGO_DB]
        db[self.MONGO_TABLE].insert(d_item)
