# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class VikkaItem(scrapy.Item):
    title = scrapy.Field()
    article_body = scrapy.Field()
    tags = scrapy.Field()
    url = scrapy.Field()
    table_date = scrapy.Field()


