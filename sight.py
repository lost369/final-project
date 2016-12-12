# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import scrapy
class TripavisorSpider(scrapy.Spider):
    name = 'tripadvisor'
    allow_domains = ['tripadvisor.com']
    start_urls=(
        'https://www.tripadvisor.com/Attractions-g298566-Activities-Osaka_Osaka_Prefecture_Kinki.html',
    )
    
    def parse(self, response):
        urls = response.xpath('//div[@class="property_title"]/a/@href').extract()
        for url in urls:
            absolute_url=response.urljoin(url)
            #yield {'url' :  absolute_url }
            yield scrapy.Request(absolute_url, callback=self.parse_restaurant)
                                 
        next_page_url= response.xpath('//a[text()="Next"]/@href').extract_first()
        next_absolute_url=response.urljoin(next_page_url)
        #yield {'url' : next_absolute_url}
        yield scrapy.Request(next_absolute_url,  callback=self.parse)
            
    def parse_restaurant(self,response):
        rating = response.xpath('//img[@property="ratingValue"]/@content').extract_first()
        name = response.xpath('//div[@class="mapContainer"]/@data-name').extract_first()
        latitude = response.xpath('//div[@class="mapContainer"]/@data-lat').extract_first()
        longitude = response.xpath('//div[@class="mapContainer"]/@data-lng').extract_first()
        texts = response.xpath('//span[@class="noQuotes"]/text()').extract()
        excellent = response.xpath('//ul[@class="barChart"]/li/div[1]/text()').extract_first()
        a=""
        for text in texts:
            a+=text+' / '
        yield { 'Rating': rating,
                'name' : name,
                'latitude' : latitude,
               'longitude' : longitude,
               'text': a,
                'excellent' : excellent
              }
        
            
    
    