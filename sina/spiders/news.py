# -*- coding: utf-8 -*-
import scrapy
from sina.items import SinaItem


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["news.sina.com.cn"]
    start_urls = (
        'http://news.sina.com.cn',
    )

    def parse(self, response):
        for href in response.xpath('//a/@href').extract():
            if href.endswith('.shtml'):
                yield scrapy.Request(href, callback=self.extract_content)

    def extract_content(self, response):
        h1s = response.xpath('//h1')
        if len(h1s) > 0:
            h1 = h1s[0]
            title = h1.xpath('text()').extract()[0]
            pub_dates = response.xpath('//*[@id="pub_date"]/text()').extract()
            if len(pub_dates) > 0:
                pub_date = pub_dates[0]
            else:
                pub_date = ''

            if pub_date == '':
                pub_dates = response.xpath(
                    '//*[@id="navtimeSource"]/text()').extract()
                pub_date = pub_dates[0] if len(pub_dates) > 0 else ''
            if pub_date == '':
                pub_dates = response.xpath(
                    '//*[@class="time"]/text()').extract()
                pub_date = pub_dates[0] if len(pub_dates) > 0 else ''

            item = SinaItem()
            item['link'] = response.url
            item['title'] = title
            item['pub_date'] = pub_date

            ps = response.xpath('//*[@id="artibody"]/p/text()').extract()
            item['body'] = ' '.join(ps)

            yield item
