import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TranscriptsSpider(CrawlSpider):
    name = 'transcripts'
    allowed_domains = ['subslikescript.com']
    start_urls = ['https://subslikescript.com/movies']

    # Setting rules for the crawler
    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='scripts-list']/a")), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        # Getting the article box that contains the data we want (title, plot, etc)
        article = response.xpath("//article[@class='main-article']")

        # Extract the data we want and then yield it
        yield {
            'title': article.xpath("./h1/text()").get(),
            'plot': article.xpath("./p/text()").get(),
            'transcript': article.xpath("./div[@class='full-script']/text()").getall(),
            'url': response.url,
        }
