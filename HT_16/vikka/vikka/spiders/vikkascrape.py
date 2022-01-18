from requests import Request

import scrapy
import datetime

from ..items import VikkaItem

from bs4 import BeautifulSoup


class WrongDate(Exception):
    pass

class VikkascrapeSpider(scrapy.Spider):
    name = 'vikkascrape'
    allowed_domains = ['vikka.ua']
    start_urls = ['http://vikka.ua/']

    def define_date(self):
        custom_date = input('Enter date (format - yyyy-mm-dd): ')
        try:
            yyyy, mm, dd = custom_date.split('-')
            if not datetime.date(int(yyyy), int(mm), int(dd)):
                raise ValueError
            elif datetime.date(int(yyyy), int(mm), int(dd)) > datetime.date.today():
                raise WrongDate
            else:
                return custom_date.split('-')
        except ValueError:
            print('Wrong date input!')
            return 'error'
        except WrongDate:
            print('This date is more than today!')
            return 'error'

    def start_requests(self):
        try:
            # 2017/11/30 есть больше 1 страницы
            input_date = self.define_date()
            if input_date == 'error':
                raise WrongDate
            table_date = f'{input_date[0]}_{input_date[1]}_{input_date[2]}'
            url = f'http://vikka.ua/{input_date[0]}/{input_date[1]}/{input_date[2]}/'
            yield scrapy.Request(
                url=url,
                callback=self.parse_news_page,
                cb_kwargs=dict(table_date=table_date)
            )
        except WrongDate:
            return 'Wrong date input!'

    def parse_news_page(self, response, table_date):
        soup = BeautifulSoup(response.text, "lxml")
        for news in soup.select('.title-cat-post a'):
            urls = news.get('href')
            yield scrapy.Request(
                url=urls,
                callback=self.parse_news,
                cb_kwargs=dict(table_date=table_date)
            )


        next_page_url = soup.select_one('.nav-links a.next.page-numbers')
        if not next_page_url:
            print('Last page!')
            return
        yield scrapy.Request(
            url=next_page_url.get('href'),
            callback=self.parse_news_page,
            cb_kwargs=dict(table_date=table_date)
        )
    def parse_news(self, news, table_date):
        article_body = ''
        soup = BeautifulSoup(news.text, "lxml")
        vikkaitems = VikkaItem()
        vikkaitems['title'] = soup.select_one('h1.post-title').text
        for i in soup.select_one('.entry-content'):
            article_body += f'{i.text}\n'
        vikkaitems['article_body'] = article_body
        vikkaitems['tags'] = ', '.join([f'#{i.text}' for i in soup.select('.post-tag')])
        vikkaitems['url'] = news.url
        vikkaitems['table_date'] = table_date
        return vikkaitems


