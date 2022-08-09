from django.contrib import admin
from .models import Top_Models
from .models import main_images
from .models import all_products, Order, OrderPosition, Profile



class ArticlesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('title', 'id',)


class OrderPositionInline(admin.TabularInline):
    model = OrderPosition
    extra = 3


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',)
    inlines = [OrderPositionInline,]



@admin.register(Profile)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user',)


admin.site.register(Top_Models, ArticlesAdmin)
admin.site.register(all_products, ArticlesAdmin)
admin.site.register(main_images, ArticlesAdmin)

