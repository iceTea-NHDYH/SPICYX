import scrapy
class NewSpider(scrapy.Spider):
    name = "new.spider"
    start_urls = ['http://http://172.18.58.80/spicyx/']