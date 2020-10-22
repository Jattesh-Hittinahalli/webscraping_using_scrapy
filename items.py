# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WallmartItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_rating = scrapy.Field()
    product_no_rating = scrapy.Field()

    #reviewer_name =scrapy.Field()
    reviewer_rating = scrapy.Field()
   # reviewer_headline = scrapy.Field()
    reviewer_comment = scrapy.Field()
    reviewed_date = scrapy.Field()
   # reviewes_likes= scrapy.Field()
    #reviewes_disslikes = scrapy.Field()






    pass
