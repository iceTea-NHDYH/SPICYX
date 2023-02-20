import scrapy
class NewSpider(scrapy.Spider):
    name = "new.spider"
    start_urls = ['http://brickset.com/sets/year-2019']
