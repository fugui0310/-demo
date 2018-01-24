# -*- coding: utf-8 -*-
import scrapy

from ..items import AmazonItem
from scrapy.http import Request
from urllib.parse import urlencode


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.cn']
    start_urls = ['http://www.amazon.cn/']

    def __int__(self, keyword=None, *args, **kwargs):
        super(AmazonSpider).__init__(*args, **kwargs)
        self.keyword = keyword

    def start_requests(self):
        url = 'https://www.amazon.cn/s/ref=nb_sb_noss_1?'
        paramas = {
            '__mk_zh_CN': '亚马逊网站',
            'url': 'search - alias = aps',
            'field-keywords': self.keyword
        }
        url = url + urlencode(paramas, encoding='utf-8')
        yield Request(url, callback=self.parse_index)

    def parse_index(self, response):
        print('解析索引页:%s' % response.url)

        urls = response.xpath('//*[contains(@id,"result_")]/div/div[3]/div[1]/a/@href').extract()
        for url in urls:
            yield Request(url, callback=self.parse_detail)
        next_url = response.urljoin(response.xpath('//*[@id="pagnNextLink"]/@href').extract_first())
        print('下一页的url', next_url)
        yield Request(next_url, callback=self.parse_index)

    def parse_detail(self, response):
        print('解析详情页:%s' % (response.url))

        item = AmazonItem()
        # 商品名字
        item['goods_name'] = response.xpath('//*[@id="productTitle"]/text()').extract_first().strip()
        # 价钱
        item['goods_price'] = response.xpath('//*[@id="priceblock_ourprice"]/text()').extract_first().strip()
        # 配送方式
        item['delivery_method'] = ''.join(response.xpath('//*[@id="ddmMerchantMessage"]//text()').extract())
        return item


    # def __int__(self,keyword=None,*args,**kwargs):
    #     super(AmazonSpider).__init__(*args,**kwargs)
    #     self.keyword=keyword
    #
    # def start_requests(self):
    #     url='https://www.amazon.cn/s/ref=nb_sb_noss_1?'
    #     paramas={
    #         '__mk_zh_CN': '亚马逊网站',
    #         'url': 'search - alias = aps',
    #         'field-keywords': self.keyword
    #     }
    #     url=url+urlencode(paramas,encoding='utf-8')
    #     yield Request(url,callback=self.parse_index)
    #
    #
    # def parse_index(self, response):
    #     print('解析索引页:%s' %response.url)
    #
    #     urls=response.xpath('//*[contains(@id,"result_")]/div/div[3]/div[1]/a/@href').extract()
    #     for url in urls:
    #         yield Request(url,callback=self.parse_detail)
    #
    #     next_url=response.urljoin(response.xpath('//*[@id="pagnNextLink"]/@href').extract_first())
    #     print('下一页的url',next_url)
    #     yield Request(next_url,callback=self.parse_index)
    #
    # def parse_detail(self,response):
    #     print('解析详情页:%s' %(response.url))
    #
    #     item=AmazonItem()
    #     # 商品名字
    #     item['goods_name'] = response.xpath('//*[@id="productTitle"]/text()').extract_first().strip()
    #     # item['goods_name'] = self.get_xpath(response,'//*[@id="productTitle"]/text()')[:100]
    #
    #     # 价钱
    #     # item['goods_price'] = self.get_xpath(response,'//*[@id="priceblock_ourprice"]/text()')
    #
    #     item['goods_price'] = response.xpath('//*[@id="priceblock_ourprice"]/text()').extract_first().strip()
    #     # 配送方式
    #     item['delivery_method'] = ''.join(response.xpath('//*[@id="ddmMerchantMessage"]//text()').extract())
    #     print('123')
    #     return item
    # #
    # # def get_xpath(self,response,xpath):
    # #     if not response.xpath(xpath).extract_first():
    # #         return ''
    # #     return response.xpath(xpath).extract_first().strip()
