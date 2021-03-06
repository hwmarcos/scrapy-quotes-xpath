# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        self.log('*****************************'+response.url)
        divs = response.xpath('/html/body/div/div[2]/div[1]/div')
        for div in divs:

            text = div.xpath('.//span[contains(@class, "text")]/text()').extract_first()
            author = div.xpath('.//small[contains(@class, "author")]/text()').extract_first()
            href = div.xpath('.//span[2]/a/@href').extract_first()

            yield {
                'text' : text,
                'author' : author,
                'href' : href
            }
