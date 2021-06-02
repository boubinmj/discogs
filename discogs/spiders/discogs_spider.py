from discogs.items import DiscogsItem
from scrapy import Spider, Request
import re

class DiscogsSpider(Spider):
    name = "discogs_spider"
    allowed_urls = ['https://www.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_Billboard_200_number-one_albums_of_2014']

    def parse(self, response):
        page_urls = [f'https://en.wikipedia.org/wiki/List_of_Billboard_200_number-one_albums_of_{i}' for i in range(1976, 1977)]

        for url in page_urls:
            yield Request(url=url, callback=self.parse_results_page)


    def parse_results_page(self, response):


        rows = response.xpath('//table[@class="wikitable plainrowheaders"]//tr')
        if(rows == []):
            rows = response.xpath('//table[2]//tr')

        for row in rows[1:]:

            try:
                album = row.xpath('./td[1]//a/text()').extract_first().strip()
                artist = row.xpath('./td[2]//a/text()').extract_first()
                if(artist is None):
                    continue
                issue_date = row.xpath('./th/text()').extract_first().strip()
            except:
                album = row.xpath('./td[2]//a/text()').extract_first()
                if(album is None or len(album) < 5):
                    continue
                artist = row.xpath('./td[3]//a/text()').extract_first()
                if(artist is None):
                    continue
                issue_date = row.xpath('./td[1]/text()').extract_first().strip()


            
            # try:
            #     issue_date = row.xpath('./th/text()').extract_first().strip()
            # except:
            #     issue_date = row.xpath('./td[1]//a/text()').extract_first()
            #     print('except issue_date')

            item = DiscogsItem()
            item['issue_date'] = issue_date
            item['album'] = album
            item['artist'] = artist

            yield item