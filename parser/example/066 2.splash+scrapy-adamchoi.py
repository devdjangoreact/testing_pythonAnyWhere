import scrapy
from scrapy_splash import SplashRequest

class AdamchoiSpider(scrapy.Spider):
    name = 'adamchoi'
    allowed_domains = ['www.adamchoi.co.uk']
    # start_urls = ['http://www.adamchoi.co.uk/']

    # Copy and paste the lua code written in splash inside the script variable
    script = '''
        function main(splash, args)
          splash.private_mode_enabled = false
          assert(splash:go(args.url))
          assert(splash:wait(3))
          all_matches = assert(splash:select_all("label.btn.btn-sm.btn-primary"))
          all_matches[2]:mouse_click()
          assert(splash:wait(3))
          splash:set_viewport_full()
          return {splash:png(), splash:html()}
        end
    '''

    # Define a start_requests function to connect scrapy and splash
    def start_requests(self):
        yield SplashRequest(url='https://www.adamchoi.co.uk/overs/detailed', callback=self.parse,
                            endpoint='execute', args={'lua_source':self.script})

    # Let's verify if the connection splash-scrapy is working getting the html
    def parse(self, response):
        print(response.body)