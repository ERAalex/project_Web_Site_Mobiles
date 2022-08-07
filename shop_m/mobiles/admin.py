from django.contrib import admin
from .models import Top_Models
from .models import main_images
from .models import all_products



class ArticlesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('title', 'id',)


admin.site.register(Top_Models, ArticlesAdmin)
admin.site.register(all_products, ArticlesAdmin)
admin.site.register(main_images, ArticlesAdmin)

