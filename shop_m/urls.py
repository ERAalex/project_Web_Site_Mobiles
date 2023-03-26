from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^cart/', include('cart.urls', namespace='cart')),
    path('', include('mobiles.urls')),
    path('', include('accounts_shop.urls')),
    path('', include('django.contrib.auth.urls')), # добавляем авторизацию по ссылке accounts


]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


