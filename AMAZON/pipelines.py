# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from .sql import Mysql


class AmazonPipeline(object):
    def process_item(self, item, spider):
        goods_name=item['goods_name']
        goods_price=item['goods_price']
        delivery_mode=item['delivery_method']
        if not Mysql.is_repeat(goods_name):
            Mysql.insert_tables_goods(goods_name,goods_price,delivery_mode)
