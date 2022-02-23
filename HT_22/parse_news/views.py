from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import News, Category, Ask, Job, Work
from .forms import SelectCategory
from . import tasks

import json


def index(request):
    if request.method == 'POST':
        form = SelectCategory(request.POST)

        if form.is_valid():
            selected_cat = request.POST['selected_cat']
            tasks.get_news_csv(selected_cat)
            return render(request, 'parse_news/done.html')
        else:
            return redirect('/')
    else:
        form = SelectCategory()
        context = {
            'form': form,
        }
        return render(request, 'parse_news/index.html', context)


def c_done(request):
        return render(request, 'parse_news/done.html')





