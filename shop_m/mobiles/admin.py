from django.contrib import admin
from .models import Top_Models
from .models import main_images
from .models import all_products
from django.utils.safestring import mark_safe



class ArticlesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('title', 'id',)

@admin.register(all_products)
class all_productAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_show', 'price', 'discount_active', 'discount']
    list_filter = ['show_item', 'price']
    list_editable = ['price', 'discount_active', 'discount']

    def image_show(self, obj):
        if obj.artimage:
            return mark_safe("<img src='{}' width='60' />".format(obj.artimage.url))
        return "Нет картинки"

    image_show.__name__ = "Картинка"



admin.site.register(Top_Models, ArticlesAdmin)
admin.site.register(main_images, ArticlesAdmin)

