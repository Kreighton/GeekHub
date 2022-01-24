"""Використовуючи бібліотеку requests написати скрейпер для отримання статей / записів із АПІ
Документація на АПІ:
https://github.com/HackerNews/API
Скрипт повинен отримувати із командного рядка одну із наступних категорій:
askstories, showstories, newstories, jobstories
Якщо жодної категорії не указано - використовувати newstories.
Якщо категорія не входить в список - вивести попередження про це і завершити роботу.
Результати роботи зберегти в CSV файл. Зберігати всі доступні поля.
Зверніть увагу - інстанси різних типів мають різний набір полів.
Код повинен притримуватися стандарту pep8.
Перевірити свій код можна з допомогою ресурсу http://pep8online.com/
Для тих, кому хочеться зробити щось "додаткове" - можете зробити наступне: другим параметром cкрипт може приймати
назву HTML тега і за допомогою регулярного виразу видаляти цей тег разом із усим його вмістом із значення атрибута "text"
(якщо він існує) отриманого запису.

"""

import requests
import json
import csv
import datetime


class WrongCategoryError(Exception):
    pass


class GetAllNews(object):
    def __init__(self):
        self.flag = True
        self.categories = ('askstories', 'showstories', 'newstories', 'jobstories')
        self.current_category = self.get_url_category()
        self.tdate = datetime.datetime.today()

    def get_url_category(self):
        url_cat = input('Enter news category (askstories, showstories, newstories, jobstories): ')
        if url_cat == '':
            return 'newstories'
        elif url_cat in self.categories:
            return url_cat
        else:
            self.flag = False

    def get_ids_list(self):
        if not self.flag:
            return
        category_url = f'https://hacker-news.firebaseio.com/v0/{self.current_category}.json'
        list_of_articles = requests.get(url=category_url).json()
        return list_of_articles

    def get_news_csv(self):
        try:
            list_of_articles = self.get_ids_list()
            if not self.flag:
                raise WrongCategoryError()

            all_news_list = []
            fieldnames = set()

            for i in list_of_articles:
                temp_url = f'https://hacker-news.firebaseio.com/v0/item/{i}.json'
                request = requests.get(url=temp_url).json()
                print(i)
                all_news_list.append(request)
                fieldnames.update(request.keys())

            fieldnames = sorted(fieldnames)
            filename = f'{self.current_category}_{self.tdate.strftime("%Y_%m_%d")}.csv'
            with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval='None')
                writer.writeheader()
                writer.writerows(all_news_list)
            csvfile.close()

        except WrongCategoryError:
            print('Selected wrong category!')
            return

if __name__ == '__main__':
    temp = GetAllNews()
    temp.get_news_csv()
