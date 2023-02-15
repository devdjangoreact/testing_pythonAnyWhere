import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TranscriptsSpider(CrawlSpider):
    name = 'transcripts'
    allowed_domains = ['subslikescript.com']
    # start_urls = ['https://subslikescript.com/movies_letter-X']

    # Setting an user-agent variable
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'

    # Editing the user-agent in the request sent
    def start_requests(self):
        yield scrapy.Request(url='https://subslikescript.com/movies_letter-X', headers={
            'user-agent':self.user_agent
        })

    # Setting rules for the crawler
    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//ul[@class='scripts-list']/a")), callback='parse_item', follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths=("(//a[@rel='next'])[1]")), process_request='set_user_agent'),
    )

    # Setting the user-agent
    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        # Getting the article box that contains the data we want (title, plot, etc)
        article = response.xpath("//article[@class='main-article']")
        # .getall() will return a list, use .join() to turn the list into a string
        transcript_list = article.xpath("./div[@class='full-script']/text()").getall()
        transcript_string = ' '.join(transcript_list)

        # Extract the data we want and then yield it
        yield {
            'title':article.xpath("./h1/text()").get(),
            'plot':article.xpath("./p/text()").get(),
            'transcript':transcript_string,
            'url':response.url,
            # 'user-agent':response.request.headers['User-Agent'],
        }
