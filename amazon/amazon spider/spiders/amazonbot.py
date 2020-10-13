import scrapy
from scrapy import Spider
from scrapy.http import Request

class AmazonbotSpider(scrapy.Spider):
    name = 'amazonbot'
    allowed_domains = ['amazon.com']
    start_urls =["https://www.amazon.com/s?k=amazon+shopping+online&i=stripbooks&rh=n%3A283155%2Cn%3A5%2Cn%3A3510&dc&adgrpid=84486094307&gclid=CjwKCAjwwab7BRBAEiwAapqpTDYtTN8aym2q_rlYn1VdmofKw0_bzkd6xjaCl8cMY4syjbPZMKNMjxoCLIYQAvD_BwE&hvadid=393524136919&hvdev=c&hvlocphy=1010294&hvnetw=g&hvqmt=b&hvrand=2170543926145783317&hvtargid=kwd-469356929&hydadcr=22365_10729094&qid=1602280766&rnid=1000&ref=sr_nr_n_11"]

    def parse(self, response):
        book = 

    def parse_book(self, response):
        books = response.xpath('//div[@class="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"]')
        for book in books:
            title = book.xpath('.//span[@class="a-size-medium a-color-base a-text-normal"]/text()').get()
            date = book.xpath('.//span[@class="a-size-base a-color-secondary a-text-normal"]/text()').get()
            try:
                reviews_no = book.xpath('.//a[@class="a-link-normal"]/span[@class="a-size-base"]/text()').get()
            except Exception:
                reviews_no = None
                reviews_no = 0
            # reviews_no = book.xpath('.//a[@class="a-link-normal"]/span[@class="a-size-base"]/text()').get()
            ratings = book.xpath('.//span[@class="a-icon-alt"]/text()').get()


            yield{'Title': title,
                'Date': date,
                'Reviews_no': reviews_no,
                'Ratings': ratings}


        #     # Processing Next Page
        next_page_url = response.xpath('//*[@class="a-last"]/a/@href').get()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)



# import scrapy


# class AmazonbotSpider(scrapy.Spider):
#     name = 'amazonbot'
#     allowed_domains = ['amazon.com']
#     start_urls =["https://www.amazon.com/s?k=amazon+shopping+online&i=stripbooks&rh=n%3A283155%2Cn%3A5%2Cn%3A3510&dc&adgrpid=84486094307&gclid=CjwKCAjwwab7BRBAEiwAapqpTDYtTN8aym2q_rlYn1VdmofKw0_bzkd6xjaCl8cMY4syjbPZMKNMjxoCLIYQAvD_BwE&hvadid=393524136919&hvdev=c&hvlocphy=1010294&hvnetw=g&hvqmt=b&hvrand=2170543926145783317&hvtargid=kwd-469356929&hydadcr=22365_10729094&qid=1602280766&rnid=1000&ref=sr_nr_n_11"]

#     def parse(self, response):
#         books = response.xpath('//div[@class="sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-28-of-32 sg-col-16-of-20 sg-col sg-col-32-of-36 sg-col-12-of-16 sg-col-24-of-28"]')
#         for book in books:
#             title = book.xpath('.//span[@class="a-size-medium a-color-base a-text-normal"]/text()').get()
#             date = book.xpath('.//span[@class="a-size-base a-color-secondary a-text-normal"]/text()').get()
#             try:
#                 reviews_no = book.xpath('.//a[@class="a-link-normal"]/span[@class="a-size-base"]/text()').get()
#             except Exception:
#                 reviews_no = None
#                 reviews_no = 0
#             # reviews_no = book.xpath('.//a[@class="a-link-normal"]/span[@class="a-size-base"]/text()').get()
#             ratings = book.xpath('.//span[@class="a-icon-alt"]/text()').get()


#             yield{'Title': title,
#                 'Date': date,
#                 'Reviews_no': reviews_no,
#                 'Ratings': ratings}


#         #     # Processing Next Page
#         next_page_url = response.xpath('//*[@class="a-last"]/a/@href').get()
#         absolute_next_page_url = response.urljoin(next_page_url)
#         yield scrapy.Request(absolute_next_page_url)
