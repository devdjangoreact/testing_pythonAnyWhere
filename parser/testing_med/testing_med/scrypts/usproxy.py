import scrapy
from scrapy_splash import SplashRequest
from scrapy import Selector

class UsProxy(scrapy.Spider):
    #identity
    name = 'usproxy'
    script = '''
    function main(splash, args)
    assert(splash:go(args.url))
    treat = require('treat')
    result = {}
    for i=1,9,1
    do
        assert(splash:runjs("document.querySelector('#proxylisttable_next a').click()"))
        result[i] = splash.html()
    end
    return treat.as_array(result)

    end
'''
    #request
    def start_requests(self):
        url = 'https://us-proxy.org'

        # get first page
        yield SplashRequest(url=url,callback=self.parse,endpoint='render.html',args={'wait':0.5})
        # Run lua script to click on the next button and return rendered html
        # dont_filter => to tell splash that the two requests are not identical and process the rest of the pages
        yield SplashRequest(url=url,callback=self.parse_other_pages,endpoint='execute',dont_filter=True,args={'wait':0.5,'lua_source':self.script})

    #response
    def parse(self,response):
        for row in response.xpath('//table[@id="proxylisttable"]/tbody/tr[@role="row"]'):
            yield {
                'ip' : row.xpath('.//td[1]/text()').extract_first(),
                'port' : row.xpath('.//td[2]/text()').extract_first(),
            }
    def parse_other_pages(self,response):
        for page in response.data:  #reponse.data returns list of html for all 9 pages and page is a string
            renderd_response = Selector(text=page)
            for row in renderd_response.xpath('//table[@id="proxylisttable"]/tbody/tr[@role="row"]'):
                yield {
                    'ip' : row.xpath('.//td[1]/text()').extract_first(),
                    'port' : row.xpath('.//td[2]/text()').extract_first(),
                }