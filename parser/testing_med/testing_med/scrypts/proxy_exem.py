# spiders/quotes.py

import scrapy
from testing_med.items import QuoteItem

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_splash import SplashRequest 

# wait
lua_script = """
function main(splash, args)
          splash:on_request(function(request)
            request:set_proxy{
              host = "45.61.187.67",
              port = 4009,
              type = "HTTP"
            }
          end
          )
          assert(splash:go(args.url))
          assert(splash:wait(5))
          assert(splash:set_viewport_full())
          return {
            html = splash:html(),
            url = splash:url(),
    				png = splash:png(),
          }
        end
"""

class QuotesSpider(CrawlSpider):
    name = 'proxy_exem'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/js/'] 

    # Setting rules for the crawler
    rules = (
        Rule(LinkExtractor(
          allow=(), restrict_xpaths=("")
          ),
             callback='start_requests', follow=True),
    )

    def start_requests(self):
        url = 'https://quotes.toscrape.com/js/'
        yield scrapy.Request(url, self.parse, meta={
                'splash': {
                    'endpoint': 'execute',
                    'args': {
                        'lua_source': lua_script,

                    }
                }
            })
 

    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.css('div.quote'):
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield quote_item
