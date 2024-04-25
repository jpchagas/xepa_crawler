import scrapy


class CeasarsSpider(scrapy.Spider):
    name = "ceasars"
    allowed_domains = ["ceasa.rs.gov.br"]
    start_urls = ["https://ceasa.rs.gov.br/"]

    def parse(self, response):
        pass
