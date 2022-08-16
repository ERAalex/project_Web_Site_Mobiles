from django.urls import path
from . import views
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

urlpatterns = [
    path('', views.index, name='index'),
    path('start', views.index, name='start'),
    path('test', views.test, name='test_test'),
    path('registr/', views.register, name='registr'),
    path('prod_show/', views.prod_pag_page, name='products'),

# блок ссылок и вьюшек для вывода конкретных моделей внутри шаблона products
    path('apple', views.apple_show, name='apple'),
    path('samsung', views.samsung_show, name='samsung'),
    path('huawei', views.huawei_show, name='huawei'),
    path('honor', views.honor_show, name='honor'),
    path('prod_chip', views.chip_show, name='prod_chip'),
    path('prod_expens', views.expensive_show, name='prod_expens'),
    path('discount', views.discount_show, name='discount'),

# просмотр каждого товара на отдельной странице
    path('<int:pk>', views.ProductDeatailView.as_view(), name='product_detail'),
    path('/top_models/<int:pk>', views.ProductTopDeatailView.as_view(), name='product_detail_top'),
]
