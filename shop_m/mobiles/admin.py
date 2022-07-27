from django.contrib import admin
from .models import Top_Models
from .models import main_images

class ArticlesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Top_Models, ArticlesAdmin)
admin.site.register(main_images, ArticlesAdmin)
