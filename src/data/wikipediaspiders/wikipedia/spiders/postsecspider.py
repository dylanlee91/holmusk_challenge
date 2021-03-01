import scrapy

class ScrapeTableSpider(scrapy.Spider):
    name = 'postsec'


    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/List_of_schools_in_Singapore',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        for row in response.xpath('//div/*[@class="wikitable"]//tbody/tr'):
            yield {
                'school_name': row.xpath('td[2]//text()').extract_first(),
                'studentpop': row.xpath('td[4]//text()').extract_first(),
            }
#testing in scrapy shell        
#for row in response.xpath('//div/*[@class="wikitable"]//tbody/tr'):print('school_name',row.xpath('td[2]//text()').extract_first())
