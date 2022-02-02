from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import News, Category, Ask, Job, Work
from .forms import SelectCategory

import requests
import json


def index(request):
    if request.method == 'POST':
        form = SelectCategory(request.POST)
        if form.is_valid():
            selected_cat = request.POST['selected_cat']
            get_news_csv(selected_cat)
            return render(request, 'parse_news/done.html')

    else:
        form = SelectCategory()
        context = {
            'form': form,
        }
        return render(request, 'parse_news/index.html', context)


def c_done(request):
        return render(request, 'parse_news/done.html')


def get_ids_list(current_category):
    category_url = f'https://hacker-news.firebaseio.com/v0/{current_category}.json'
    list_of_articles = requests.get(url=category_url).json()
    return list_of_articles


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


