import scrapy

class MaskSpider(scrapy.Spider):
    name = "masks"
    start_urls=[
        'https://www.amazon.in/s?k=clothes+for+men',
        ]

    def parse(self, response):
        for product in response.xpath('//div[@data-component-type="s-search-result"]/div/span/div/div'):
            yield {
                'image_link': product.xpath('//span[@class="rush-component"]/a[@class="a-link-normal"]/div/img/@src').get(),
                'product_url' : product.xpath('//span[@class="rush-component"]/a[@class="a-link-normal"]/@href').get(),
                'product_name' : product.xpath('/div[3]/h2/a/span/text()').get(),
                'price' : product.xpath('/div[5]/div//a/span[@class="a-price"]/span[2]/span[2]/text()').get(),
                }
        next_page=response.xpath('/html/body/div[1]/div[2]/div[1]/div[2]/div/span[3]/div[2]/div[62]/span/div/div/ul/li[7]/a/@href').extract()
        if next_page is not None:
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

        
            

