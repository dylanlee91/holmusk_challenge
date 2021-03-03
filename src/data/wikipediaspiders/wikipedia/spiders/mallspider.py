import scrapy

class ScrapeTableSpider(scrapy.Spider):
    name = 'malls'

    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/List_of_shopping_malls_in_Singapore',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
 
    def parse(self, response):
        yield {
                'malls' : response.xpath('//*[@class="div-col"]/ul/li//text()').extract()
            }

#testing in scrapy shell        
#for row in response.xpath('//*[@class="div-col"]/ul'): print(row.xpath('/li//text()').extract())