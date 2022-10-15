from django.contrib import admin
from .models import *


class VuqesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


class AddAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('name',)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'date')
    list_display_links = ('comment', 'date')
    search_fields = ('comment', 'date')


admin.site.register(Point, VuqesAdmin)
admin.site.register(Add, AddAdmin)
admin.site.register(Comment, CommentAdmin)
