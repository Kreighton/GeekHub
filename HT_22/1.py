import requests, json


curent_models = ['newstories', 'askstories', 'jobstories', 'showstories']

for i in curent_models:
    category_url = f'https://hacker-news.firebaseio.com/v0/{i}.json'
    c_request = requests.get(url=category_url).json()
    if not c_request:
        continue
    else:
        print(len(c_request))