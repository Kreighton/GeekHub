from django.urls import path


from . import views

other_app = 'products'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    #path('', views.main, name='main'),

]