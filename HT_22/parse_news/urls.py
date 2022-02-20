from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('done/', views.c_done, name='c_done'),
]