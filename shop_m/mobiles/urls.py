from django.urls import path
from . import views
from mobiles.views import products
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

urlpatterns = [
    path('', views.index, name='index'),
    path('start', views.index, name='start'),
    path('test', views.test, name='test_test'),
    path('registr/', views.register, name='registr'),
    path('products', products, name='products'),
    path(r'^page/(\d+)/$', views.prod_list, name='prod_pagination'),

# блок ссылок и вьюшек для вывода конкретных моделей внутри шаблона products
    path('apple', views.apple_show, name='apple'),
    path('samsung', views.samsung_show, name='samsung'),
    path('huawei', views.huawei_show, name='huawei'),
    path('prod_chip', views.chip_show, name='prod_chip'),
    path('prod_expens', views.expensive_show, name='prod_expens'),

# просмотр каждого товара на отдельной странице
    path('<int:pk>', views.ProductDeatailView.as_view(), name='product_detail'),


]
