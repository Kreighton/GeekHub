from django.contrib import admin
from .models import Category, News, Ask, Job, Work


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_fk', 'by', 'title')
    search_fields = ('id',)
    list_filter = ('by',)


admin.site.register(Category)

admin.site.register(News, NewsAdmin)
admin.site.register(Ask, NewsAdmin)
admin.site.register(Job, NewsAdmin)
admin.site.register(Work, NewsAdmin)