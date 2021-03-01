import scrapy

class ScrapeTableSpider(scrapy.Spider):
    name = 'jcs'

    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/List_of_schools_in_Singapore',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        for row in response.xpath('//center/*[@class="wikitable"]//tbody/tr'):
            yield {
                'area' : row.xpath('td[2]//text()').extract_first(),
                'school_name': row.xpath('td[4]//text()').extract_first(),
                'address' : row.xpath('td[8]//text()').extract_first(),
                'schooltype' : row.xpath('td[9]//text()').extract_first()
            }

#testing in scrapy shell        
#for row in response.xpath('//center/*[@class="wikitable"]//tbody/tr'):print('area',row.xpath('td[2]//text()').extract_first(),'school_name',row.xpath('td[4]//text()').extract_first(),'address',row.xpath('td[8]//text()').extract_first(),'schooltype',row.xpath('td[9]//text()').extract_first())