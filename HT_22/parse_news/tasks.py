import logging
import requests
import os

from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from .models import News, Ask, Job, Work, Category
from HT_22.app.celery import app


def get_ids_list(current_category):
    category_url = f'https://hacker-news.firebaseio.com/v0/{current_category}.json'
    list_of_articles = requests.get(url=category_url).json()
    return list_of_articles

@app.task
def get_news_csv(current_category):
    ids_list = [i.id for i in News.objects.all()]
    ids_list.append([i.id for i in Ask.objects.all()])
    ids_list.append([i.id for i in Job.objects.all()])
    ids_list.append([i.id for i in Work.objects.all()])

    curent_models = {'newstories': News(), 'askstories': Ask(), 'jobstories': Job(), 'showstories': Work()}
    news = curent_models[current_category]

    list_of_articles = get_ids_list(current_category)
    category_list = {i.cus_cat: i.id for i in Category.objects.all()}

    for i in list_of_articles:
        if i in ids_list:
            continue

        temp_url = f'https://hacker-news.firebaseio.com/v0/item/{i}.json'
        c_request = requests.get(url=temp_url).json()

        if not c_request:
            continue

        for k, v in c_request.items():
            setattr(news, k, v)
            news.category_fk_id = category_list[current_category]
            news.save()
    return