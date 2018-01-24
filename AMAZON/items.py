# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 商品名字
    goods_name = scrapy.Field()
    # 价钱
    goods_price = scrapy.Field()
    # 配送方式
    delivery_method = scrapy.Field()