import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    # allowed_domains = ['https://www.amazon.com/product-reviews/B00YFTHJ9C/ref=acr_dp_hist_5?ie=UTF8&filterByStar=five_star&reviewerType=all_reviews#reviews-filter-bar']
    myBaseUrl = "https://www.amazon.com/AmazonBasics-8-Sheet-Cross-Cut-Credit-Shredder/product-reviews/B00YFTHJ9C/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="
    
    start_urls = []
    # Creating list of urls to be scraped by appending page number a the end of base url
    for i in range(1,101):
        start_urls.append(myBaseUrl+str(i))
        
    def parse(self, response):
            data = response.css('#cm_cr-review_list')
            # Collecting product star ratings
            star_rating = data.css('.review-rating')
            # Collecting user reviews
            comments = data.css('.review-text')
            count = 0
            # Combining the results
            for review in star_rating:
                yield{'stars': ''.join(review.xpath('.//text()').extract()),
                      'comment': ''.join(comments[count].xpath(".//text()").extract()).strip()
                     }
                count=count+1
            