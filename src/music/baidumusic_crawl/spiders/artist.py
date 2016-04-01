# -*- coding: utf-8 -*-
import scrapy
from ..items import BaidumusicItem


class ArtistSpider(scrapy.Spider):
    name = "artist"
    allowed_domains = ["baidu.com/artist"]
    start_urls = (
        'http://music.baidu.com/artist/',
    )

    def parse(self, response):
        li = response.xpath('//li')
        for li_info in li:
            try:
                artist = li_info.xpath('a/text()').extract()[0]
                link = li_info.xpath('a/@href').extract()[0]
                letter_index = li_info.xpath('../../h3/text()').extract()[0]
                item = BaidumusicItem()
                item['artist'] = artist
                item['link'] = r'http://music.baidu.com' + link
                item['letter_index'] = letter_index
                yield item
            except:
                continue
