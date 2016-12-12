import scrapy
class TripavisorSpider(scrapy.Spider):
    name = 'restaurant'
    allow_domains = ['tripadvisor.com']
    start_urls=(
        'https://www.tripadvisor.com/Restaurants-g298566-Osaka_Osaka_Prefecture_Kinki.html',
    )
    
    def parse(self, response):
        urls = response.xpath('//h3[@class="title"]/a/@href').extract()
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
        money = response.xpath('//div[@class="heading_details"]/div[1]/text()').extract()
        features = response.xpath('//div[@class="heading_details"]/div[2]/a/text()').extract()
        excellent = response.xpath('//*[@id="ratingFilter"]/ul/li[1]/label/span[2]/text()').extract()
        texts = response.xpath('//span[@class="noQuotes"]/text()').extract()
        a=""
        b=""
        for text in texts:
           a+=text+' / '
        for text in features:
            b+=text+' / '

        yield {'Rating': rating,
                'name' : name,
                'latitude' : latitude,
                'longitude' : longitude,
                'text' : a,
                'excellent' : excellent,
                'money' : money,
                'feature' : b
              }
            
    
    