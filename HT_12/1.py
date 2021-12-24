'''1. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи:
   цитата, автор, інфа про автора... Отриману інформацію зберегти в CSV файл та в базу. Результати зберегти в репозиторії.
   Пагінацію по сторінкам робити динамічною (знаходите лінку на наступну сторінку і берете з неї URL). Хто захардкодить
   пагінацію зміною номеру сторінки в УРЛі - буде наказаний ;)

   '''

import os
import requests
from bs4 import BeautifulSoup
import lxml
import csv
import sqlite3


def load_to_db(quotes, authors, authors_info):
    print('Loading data to database...')
    if os.path.isfile('parsed_data.db'):
        os.remove('parsed_data.db')
    con = sqlite3.connect('parsed_data.db')
    cur = con.cursor()
    cur.execute('create table quotes (id integer primary key autoincrement, author_name text, author_quote text)')
    cur.execute(
        'create table authors (id integer primary key autoincrement, author_name text, author_birth text, author_desc)')
    con.commit()
    for i in range(len(authors)):
        cur.execute('INSERT INTO quotes(author_name, author_quote) VALUES(?, ?)', (authors[i], quotes[i]))
        temp_authors = cur.execute('SELECT author_name FROM authors').fetchall()
        if authors_info[i] not in temp_authors:
            cur.execute('INSERT INTO authors(author_name, author_birth, author_desc) VALUES(?, ?, ?)',
                        (authors_info[i][0], authors_info[i][1], authors_info[i][2]))
    con.commit()
    con.close()
    return 'Done!'


def load_to_csv(quotes, authors, authors_info):
    print('Loading data to .CSV file...')
    with open('authors.csv', 'w', encoding="utf-8") as temp:
        temp.write('Author name|Quote|Birth|Description\n')
        for i in range(len(quotes)):
            csv.writer(temp, delimiter='|').writerow([authors[i], quotes[i], authors_info[i][1], authors_info[i][2]])
        temp.close()
        return 'Done!'


def pagination_request(page='1iu2hg3khjl1h23ilu1hkl23'):
    if page == '1iu2hg3khjl1h23ilu1hkl23':
        page_html = requests.get('https://quotes.toscrape.com/')
    else:
        page_html = requests.get(f'https://quotes.toscrape.com{page}')
    soup = BeautifulSoup(page_html.text, 'lxml')
    return soup


def get_author(author_url):
    auth_rq = requests.get(f'https://quotes.toscrape.com{author_url}')
    soup = BeautifulSoup(auth_rq.text, 'lxml')
    author_name = soup.select_one('h3.author-title').text.strip()
    author_birth = f"{soup.select_one('span.author-born-date').text.strip()}, {soup.select_one('span.author-born-location').text.strip()}"
    author_desc = soup.select_one('div.author-description').text.strip()
    authors_total = [author_name, author_birth, author_desc]
    return authors_total


def parse_authors():
    quotes = []
    authors = []
    author_urls = []
    authors_info = []
    next_page = '1iu2hg3khjl1h23ilu1hkl23'

    while True:
        soup = pagination_request(next_page)
        author_urls.extend([i.get('href') for i in soup.select('.quote span a')])
        quotes.extend([i.text for i in soup.select('.quote span.text')])
        authors.extend([i.text for i in soup.select('small.author')])
        print('...')
        if not soup.select_one('.next a'):
            print('Completed. Starting to parse authors info.')
            for i in author_urls:
                author_csv = get_author(i)
                authors_info.append(author_csv)
                print(f'Finished {author_csv[0]}')
            break
        next_page = soup.select_one('.next a').get('href')
    print(load_to_csv(quotes, authors, authors_info))
    print(load_to_db(quotes, authors, authors_info))
    print('Success! Closing the script.')
    return

parse_authors()
