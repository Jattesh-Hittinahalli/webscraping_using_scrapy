# -*- coding: utf-8 -*-
import scrapy
from ..items import WallmartItem


class WallSpiderSpider(scrapy.Spider):
    name = 'wallspider'
    i = 1

    lastpage = 60 #you can change acccourding to your requirement

    #imp note only add product number not whole URL (last all digits after slash in the link)
    product_no = 429888532 #you can change acccourding to your product

    page_number=2 #dont Change Page number because it is assignment variable
    #dont change URL Only change product number
    start_urls = ['https://www.walmart.com/reviews/product/'+str(product_no)+'?page=1']



    def parse(self, response):
        #print("before loop")

        print(WallSpiderSpider.i)
        #global reviewer_rating
        items =WallmartItem()
        while(WallSpiderSpider.i==1):
            i=WallSpiderSpider.i+1
           # print(WallSpiderSpider.i)
            product_name = response.css('.LinesEllipsis').css('::text').extract()[0]
            product_price = response.css('.price-mantissa , .price-characteristic').css('::text').extract()[0:2]
            product_rating = response.css('.product-review-ratings .font-bold').css('::text').extract()[0]
            product_no_rating = response.css('.RatingFilter').css('::text').extract()
            items['product_name'] = product_name
            items['product_price'] = product_price
            items['product_rating'] = product_rating
            items['product_no_rating'] = product_no_rating
            WallSpiderSpider.i+=1





        #reviewer_name = response.css('.review-footer-userNickname').css('::text').extract()
        reviewer_rating = (response.css('span.seo-avg-rating').css('::text').extract()[6:])
       # reviewer_headline = response.css('.review-title').css('::text').extract()
        reviewer_comment = response.css('.review-body-text').css('::text').extract()
        reviewed_date = response.css('.review-footer-submissionTime').css('::text').extract()
       # reviewes_likes = (response.css('.s-margin-top .xxs-padding-sides').css('::text').extract())
       # reviewes_disslikes = (response.css('.s-margin-ends .xxs-padding-sides').css('::text').extract())
        next_page = 'https://www.walmart.com/reviews/product/'+str(WallSpiderSpider.product_no)+'?page=' + str(WallSpiderSpider.page_number) + ''

        if(WallSpiderSpider.page_number<=WallSpiderSpider.lastpage):
            WallSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)






       # items['reviewer_name'] = reviewer_name
        items['reviewer_rating'] = reviewer_rating
       # items['reviewer_headline'] = reviewer_headline

        items['reviewed_date'] = reviewed_date
        items['reviewer_comment'] = reviewer_comment
       # items['reviewes_likes'] = reviewes_likes
        #items['reviewes_disslikes'] = reviewes_disslikes








        yield items




















