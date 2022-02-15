from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'orders', views.OrderViewSet)

app_name = 'products'

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('', views.homepage, name='homepage'),
    path('<slug:slug>', views.homepage, name='homepage_category'),
    path('product/<int:pk>', views.product_details, name='product_details'),
    path('add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('commit-order/', views.commit_order, name='commit_order'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)