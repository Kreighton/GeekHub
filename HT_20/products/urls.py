from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<slug:slug>', views.homepage, name='homepage_category'),
    path('product/<slug:slug>', views.product_details, name='product_details'),
    path('<str:slug>/add', views.add_to_cart, name='add_to_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)