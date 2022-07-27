from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test_test'),
    # path('news', views.news_sitio, name='news_sitio'),


]
