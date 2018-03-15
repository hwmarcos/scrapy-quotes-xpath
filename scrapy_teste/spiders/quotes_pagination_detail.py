# -*- coding: utf-8 -*-
import scrapy


class QuotesPaginationDetailSpider(scrapy.Spider):
    name = 'quotes_pagination_detail'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        self.log('*****************************' + response.url)
        divs = response.xpath('/html/body/div/div[2]/div[1]/div')

        for div in divs:
            href = div.xpath('.//span[2]/a/@href').extract_first()
            detail_url = response.urljoin(href)
            yield scrapy.Request(
                detail_url,
                callback=self.parse_detail
            )

        next_page = response.xpath('//li[contains(@class, "next")]/a/@href').extract_first()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_detail(self, response):
        # self.log('*****************************' + response.url)
        author = response.xpath('/html/body/div/div[2]/h3/text()').extract_first()
        birthday = response.xpath('/html/body/div/div[2]/p[1]/span[1]/text()').extract_first()
        city = response.xpath('/html/body/div/div[2]/p[1]/span[2]/text()').extract_first()
        descr = response.xpath('//html/body/div/div[2]/div/text()').extract_first()

        yield {
            'author': author,
            'birthday': birthday,
            'city': city,
            'descr': descr,
        }