from django.contrib import admin
from .models import main_images, all_products, Articles
from django.utils.safestring import mark_safe


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ['title', 'show_item', 'date']


@admin.register(all_products)
class all_productAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_show', 'price', 'discount_active', 'discount']
    list_filter = ['show_item', 'price']
    list_editable = ['price', 'discount_active', 'discount']

# делаем так, чтобы отображались картинки в admin вместо просто ссылки на картинку, url
    def image_show(self, obj):
        if obj.artimage:
            return mark_safe("<img src='{}' width='60' />".format(obj.artimage.url)) # безопасный метод возврата строки, импортировали выше
        return "Нет картинки"

    image_show.__name__ = "Картинка"


admin.site.register(main_images)

