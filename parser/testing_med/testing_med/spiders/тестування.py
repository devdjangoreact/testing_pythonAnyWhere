import scrapy
# from testing_med.items import TestsItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_splash import SplashRequest 

lua_script = """
    function main(splash, args)
        assert(splash:go(args.url))
        assert(splash:wait(6))
        return {
        html = splash:html(),
        }
    end
"""


class QuotesSpider(CrawlSpider):
    name = 'тестування'
    allowed_domains = ['xn--80adi8aaufcj8j.xn--j1amh']
    start_urls = ['https://xn--80adi8aaufcj8j.xn--j1amh/testing/topic/7-bukleti/krok-ukr'] 

    rules = (
        Rule(LinkExtractor(
            allow =('/testing/collection/'),
            restrict_xpaths=("//div[@class='py-12']")
            ), 
            callback='start_requests', follow=False),      
    )
    
    def start_requests(self):
        url = 'https://xn--80adi8aaufcj8j.xn--j1amh/testing/topic/7-bukleti/krok-ukr'
        yield scrapy.Request(url, self.parse_link_category, meta={
                'splash': {
                    'endpoint': 'execute',
                    'args': {
                        'lua_source': lua_script,
                    }
                },
            })
    
    # create links
    def parse_link_category(self, response):
        
        items = response.xpath('.//div[@class="bg-white overflow-hidden shadow-sm sm:rounded-lg mt-5 "]')
        
        link = ''
        title = ''
        list_links = []
        for path_link in items:
            
            link = path_link.xpath('.//a[3]/@href').get()
            title = path_link.xpath(".//p[@class='text-lg font-bold']/text()").get()
            title = " ".join(title.split())
            answer_yield = yield scrapy.Request(link, callback=self.parse_item, meta={'title': title, 
                                                                       "link":link,
                                                                        'count':None, 
                                                                        'count_element':None,
                                                                       'questions': None,
                                                                       'splash': {'endpoint': 'execute',
                                                                                  'args': {
                                                                                      'lua_source': lua_script,
                                                                                      }
                                                                                    }
                                                                                  })
            list_links.append(answer_yield)
            
        yield list_links
            
            

    # # parsing
    def parse_item(self, response):
         
        link = response.meta['link'] 
        title = response.meta['title']     
                                              
        questions = response.meta['questions']
        if questions==None:
            questions = []

        items = response.xpath('//div[@class="bg-white mt-1 p-1 md:mt-5 md:p-5"]')       

        for path_link in items:
            
            nomber = path_link.xpath(".//div[contains(@class, 'text-left font-bold')]/text()").get()
            nomber = " ".join(nomber.split())            
            
            question = path_link.xpath(".//div[contains(@class, 'text-justify')]/text()").get()
            question = " ".join(question.split())                
            n = 0
            answers = []
            while n < 5:
                
                n = n + 1
 
                choise = path_link.xpath(f".//div[contains(@class, 'flex p-3 cursor-pointer hover:bg-gray-100')][{n}]/div[1]/text()").get()
                try:
                    choise = " ".join(choise.split())                
                except:
                    ''
                     
                answer = path_link.xpath(f".//div[contains(@class, 'flex p-3 cursor-pointer hover:bg-gray-100')][{n}]/div[2]/text()").get()
                try:
                    answer = " ".join(answer.split())                
                except:
                    ''
                    
                if choise == '100%':
                    choise = True
                else:
                    choise = False
                
                
                answers.append({'sort':n, 'answer':answer, 'choise':choise})
            
            questions.append({'nomber':nomber, 'question':question , 'answers':answers})
#        
#        count_element = response.meta['count_element'] 
#        
#        if count_element==None or count_element==0:
#            count_element = len(response.xpath('.//ul[contains(@class, "flex")]/li'))
#        print('>>>count_element', count_element)
#        count = response.meta['count'] 
#        
#        print('>>>count', count)
#        print('>>>title', title)
#        print('>>>link', link)
#        if count==None:
#            count = 1
#        else:
#            link = link[0:-7]
#        count = count + 1
##        if count == count_element:
                        
        yield {
            'title':title,
            "link":link,
            'questions':questions
        }
            
#        else:
#            
#            yield scrapy.Request(link+"?page="+str(count), callback=self.parse_item, meta={'title': title, 
#                                                                    "link":link+"?page="+str(count),
#                                                                    'count':count,
#                                                                    'count_element':count_element, 
#                                                                    'questions': questions,
#                                                                    'splash': {'endpoint': 'execute',
#                                                                                'args': {
#                                                                                    'lua_source': lua_script,
#                                                                                    }
#                                                                                }
#                                                                            })
