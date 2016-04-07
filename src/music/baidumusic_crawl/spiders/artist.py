# -*- coding: utf-8 -*-
import scrapy
from ..items import BaidumusicItem
from django.db import transaction
from musician.models import Musicians

class ArtistSpider(scrapy.Spider):
    name = "artist"
    allowed_domains = ["baidu.com/artist"]
    start_urls = (
        'http://music.baidu.com/artist/',
    )

    @transaction.atomic
    def parse(self, response):
        li = response.xpath('//li')
        for li_info in li:
            try:
                artist = li_info.xpath('a/text()').extract()[0]
                link = li_info.xpath('a/@href').extract()[0]
                letter_index = li_info.xpath('../../h3/text()').extract()[0]
                music_artist, created = Musicians.objects.get_or_create(name=artist)
                if music_artist.link_url != r'http://music.baidu.com' + link:
                    music_artist.link_url = r'http://music.baidu.com' + link
                    music_artist.save()
                if music_artist.letter_index != letter_index:
                    music_artist.letter_index = letter_index
                    music_artist.save()


                #item = BaidumusicItem()
                #item['artist'] = artist
                #item['link'] = r'http://music.baidu.com' + link
                #item['letter_index'] = letter_index

                yield
            except:
                continue

