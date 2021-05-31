# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DiscogsItem(scrapy.Item):
    issue_date = scrapy.Field()
    album = scrapy.Field()
    artist = scrapy.Field()
