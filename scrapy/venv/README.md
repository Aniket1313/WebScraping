In this project I make use of Python Scrapy and how to create a spider to crawl websites to scrape and structure data.

Site scraped :https://blog.scrapinghub.com/ into posts.json

ELememts fetched
title
date
author

**Setup**

Commands used:

pip install scrapy

scrapy startproject postscrape

cd postscrape

Create spiders/posts_spider.py

scrapy crawl posts

**Script--filename :posts_spider** 
path :postscrape/spiders/posts_spider.py

import scrapy


class PostsSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        'https://blog.scrapinghub.com/'
    ]

    def parse(self, response):
        for post in response.css('div.post-item'):
            yield {
                'title': post.css('.post-header h2 a::text')[0].get(),
                'date': post.css('.post-header a::text')[1].get(),
                'author': post.css('.post-header a::text')[2].get()
            }
        next_page = response.css('a.next-posts-link::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

