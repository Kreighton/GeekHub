import bs4
import requests
import lxml

url = 'https://ek.ua/ua/list/248/'

session = requests.session()
response = session.get(url)

soup = bs4.BeautifulSoup(response.text, 'lxml')
products = soup.select('.model-short-block')