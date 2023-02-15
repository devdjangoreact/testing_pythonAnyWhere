import scrapy


class WorldometersSpider(scrapy.Spider):
    name = 'worldometers'
    allowed_domains = ['www.worldometers.info/']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        # Extracting "a" elements for each country
        countries = response.xpath('//td/a')

        # Looping through the countries list
        for country in countries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # return data extracted
            yield {
                'country_name': country_name,
                'link': link,
            }