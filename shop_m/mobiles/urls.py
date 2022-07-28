from django.urls import path
from . import views
from mobiles.views import products

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test_test'),
    path('registr/', views.register, name='registr'),
    path('products', products, name='products'),


]
