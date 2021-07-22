from django.contrib import admin
from django.utils.html import format_html  # для отображения фото в админке
from .models import *


@admin.register(Post)
class BoardAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 50px; height: 50px;"/>'.format(obj.image.url))
    image_tag.short_description = 'изображение'

    date_hierarchy = 'created'
    list_display = ['name', 'description', 'created', 'image_tag', 'owner']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'email', 'created', 'active']
    list_filter = ['post', 'created', 'body', 'active']
    search_fields = ['name', 'email', 'body', 'active']
