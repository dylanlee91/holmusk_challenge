import scrapy

class ScrapeTableSpider(scrapy.Spider):
    name = 'unis'

    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/List_of_universities_in_Singapore',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        for row in response.xpath('//div/*[@class="wikitable"][1]//tbody/tr'):
            
            yield {
                'school_name': row.xpath('td[1]/a//text()').extract_first(),
                'abbrev': row.xpath('td[2]//text()').extract_first(),
                'studentpop' : row.xpath('td[3]//text()').extract_first(),
                'schooltype' : row.xpath('td[4]//text()').extract_first(),
                'founded': row.xpath('td[5]//text()').extract_first(),
            }

#testing in scrapy shell        
#for row in response.xpath('//div/*[@class="wikitable"][1]//tbody/tr'):print('school_name',row.xpath('td[1]/a//text()').extract_first(),'abbrev',row.xpath('td[2]//text()').extract_first(),'studentpop',row.xpath('td[3]//text()').extract_first(),'schooltype',row.xpath('td[4]//text()').extract_first(),'founded',row.xpath('td[5]//text()').extract_first())
