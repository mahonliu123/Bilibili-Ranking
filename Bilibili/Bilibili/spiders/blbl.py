# -*- coding: utf-8 -*-
import scrapy
from ..items import BilibiliItem
from urllib.parse import urlencode
import json


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili2'
    allowed_domains = ['bilibili.com']

    def start_requests(self):
        basic_url = 'https://api.bilibili.com/x/web-interface/ranking?'
        all_list = [0, 1, 168, 3, 129, 4, 36, 188, 160, 119, 155, 5, 181]
        for type in [1, 2, 3]:
            for rid in all_list:
                data = {
                    'rid': rid,
                    'day': 3,
                    'type': type,
                    'arc_type': 0,
                    'jsonp': 'jsonp'
                }
                if type == 1:
                    all_url = basic_url + urlencode(data)
                    yield scrapy.Request(url=all_url, callback=self.parse_all)
                elif type == 2:
                    origin_url = basic_url + urlencode(data)
                    yield scrapy.Request(url=origin_url, callback=self.parse_origin)
                else:
                    rookie_url = basic_url + urlencode(data)
                    yield scrapy.Request(url=rookie_url, callback=self.parse_rookie)
        bangumi_url = 'https://api.bilibili.com/pgc/web/rank/list?'
        for st in [1, 4]:
            formdata = {
                'day': 3,
                'season_type': st
            }
            bangumi_url = bangumi_url + urlencode(formdata)
            yield scrapy.Request(url=bangumi_url, callback=self.parse_bangumi)
        for i in [177, 23, 11]:
            cinema_url = 'https://www.bilibili.com/index/rank/all-3-{0}.json'.format(i)
            yield scrapy.Request(cinema_url, callback=self.parse_cinema)

    def parse_all(self, response):
        item = BilibiliItem()
        json_data = json.loads(response.body.decode())
        for i, data in enumerate(json_data.get('data').get('list')):
            item['number'] = i
            item['title'] = data['title']
            item['author'] = data['author']
            item['av'] = 'https://www.bilibili.com/video/av{0}/'.format(data['aid'])
            item['play_times'] = data['play']
            item['score'] = data['pts']
            yield item

    def parse_origin(self, response):
        item = BilibiliItem()
        json_data = json.loads(response.body.decode())
        for i, data in enumerate(json_data.get('data').get('list')):
            item['number'] = i
            item['title'] = data['title']
            item['author'] = data['author']
            item['av'] = 'https://www.bilibili.com/video/av{0}/'.format(data['aid'])
            item['play_times'] = data['play']
            item['score'] = data['pts']
            yield item

    def parse_bangumi(self, response):
        item = BilibiliItem()
        json_data = json.loads(response.body.decode())
        for data in json_data.get('result').get('list'):
            item['number'] = data['rank']
            item['title'] = data['title']
            item['author'] = data['copyright']
            item['av'] = data['url']
            item['play_times'] = data['stat']['view']
            item['score'] = data['pts']
            yield item

    def parse_cinema(self, response):
        item = BilibiliItem()
        json_data = json.loads(response.body.decode())
        for i, data in enumerate(json_data.get('rank').get('list')):
            item['number'] = i
            item['title'] = data['title']
            item['author'] = data['author']
            item['av'] = 'https://www.bilibili.com/video/av{0}/'.format(data['aid'])
            item['play_times'] = data['play']
            item['score'] = data['pts']
            yield item


    def parse_rookie(self, response):
        item = BilibiliItem()
        json_data = json.loads(response.body.decode())
        for i, data in enumerate(json_data.get('data').get('list')):
            item['number'] = i
            item['title'] = data['title']
            item['author'] = data['author']
            item['av'] = 'https://www.bilibili.com/video/av{0}/'.format(data['aid'])
            item['play_times'] = data['play']
            item['score'] = data['pts']
            yield item
