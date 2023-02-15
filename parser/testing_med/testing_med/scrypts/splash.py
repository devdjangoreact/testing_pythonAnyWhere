# spiders/quotes.py

import scrapy
from testing_med.items import QuoteItem

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_splash import SplashRequest 

# wait
lua_script = """
function main(splash, args)
  assert(splash:go(args.url))

  while not splash:select('div.quote') do
    splash:wait(0.1)
    print('waiting...')
  end
  return {html=splash:html()}
end
"""

class QuotesSpider(CrawlSpider):
    name = 'quotes'
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
        yield SplashRequest(url, callback=self.parse)

    def parse(self, response):
        quote_item = QuoteItem()
        for quote in response.css('div.quote'):
            quote_item['text'] = quote.css('span.text::text').get()
            quote_item['author'] = quote.css('small.author::text').get()
            quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
            yield quote_item














# # Scrolling 
# lua_script = '''
# function main(splash)
#     local num_scrolls = 10
#     local scroll_delay = 1.0

#     local scroll_to = splash:jsfunc("window.scrollTo")
#     local get_body_height = splash:jsfunc(
#         "function() {return document.body.scrollHeight;}"
#     )
#     assert(splash:go(splash.args.url))
#     splash:wait(splash.args.wait)

#     for _ = 1, num_scrolls do
#         scroll_to(0, get_body_height())
#         splash:wait(scroll_delay)
#     end        
#     return splash:html()
# end'''


    # def start_requests(self):
    #     url = 'https://quotes.toscrape.com/scroll'
    #     yield SplashRequest(
    #         url, 
    #         callback=self.parse, 
    #         endpoint='execute', 
    #         args={'wait': 0.5, 
    #               'lua_source': lua_script,  
    #               url :'https://quotes.toscrape.com/scroll',
    #               'proxy': 'http://50.219.108.3:80'
    #               }
    #         )


    # def parse(self, response):
    #     quote_item = QuoteItem()
    #     for quote in response.css('div.quote'):
    #         quote_item['text'] = quote.css('span.text::text').get()
    #         quote_item['author'] = quote.css('small.author::text').get()
    #         quote_item['tags'] = quote.css('div.tags a.tag::text').getall()
    #         yield quote_item


# # Click Page Elements
# lua_script = """
# function main(splash,args)
#     assert(splash:go(args.url))

#     local element = splash:select('body > div > nav > ul > li > a')
#     element:mouse_click()
    
#     splash:wait(splash.args.wait)  
#     return splash:html()
# end
# """



# # Take Screenshot
# class QuotesSpider(scrapy.Spider):
#     name = 'quotes_screenshot'

#     def start_requests(self):
#         url = 'https://quotes.toscrape.com/js/'
#         yield SplashRequest(
#             url, 
#             callback=self.parse, 
#             endpoint='render.json', 
#             args={
#                 'html': 1, 
#                 'png': 1, 
#                 'width': 1000,
#             })

#     def parse(self, response):
#         imgdata = base64.b64decode(response.data['png'])
#         filename = 'some_image.png'
#         with open(filename, 'wb') as f:
#             f.write(imgdata)



# # Proxies 
# lua_script = """
# splash:on_request(function(request)
#     request:set_proxy{
#         host = http://us-ny.proxymesh.com,
#         port = 31280,
#         username = username,
#         password = secretpass,
#     }
#     return splash:html()
# end)
# """



# # Running JavaScript Scripts
# javascript_script = """
# element = document.querySelector('h1').innerHTML = 'The best quotes of all time!'
# """

# class QuotesSpider(scrapy.Spider):
#     name = 'quotes'

#     def start_requests(self):
#         url = 'https://quotes.toscrape.com/js/'
#         yield SplashRequest(
#             url, 
#             callback=self.parse, 
#             endpoint='render.json', 
#             args={
#                 'wait': 2,
#                 'js_source': javascript_script, 
#                 'html': 1, 
#                 'png': 1, 
#                 'width': 1000,
#             })

#     def parse(self, response):
#         imgdata = base64.b64decode(response.data['png'])
#         filename = 'some_image.png'
#         with open(filename, 'wb') as f:
#             f.write(imgdata)
