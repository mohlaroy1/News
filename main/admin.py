from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title',)



