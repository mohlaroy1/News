from django.contrib import admin
from django.utils.html import format_html
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


class ContextInline(admin.TabularInline):
    model = Context
    extra = 1


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title', 'slug', 'views', 'read_time', 'author', 'category', 'published', 'important', 'created_at', 'get_cover',)
    list_filter = ('author', 'category', 'tags', 'published',)
    search_fields = ('title', 'intro',)
    inlines = [ContextInline, CommentInline]

    def get_cover(self, obj):
        if obj.cover:
            return format_html(
                '<img src="{}" width="80px" height="45px" style="object-fit: cover;border-radius: 6px;" />',
                obj.cover.url
            )
        return "No image"



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'name', 'email', 'text',)
    list_filter = ('article', 'name', 'email',)
    search_fields = ('article', 'name',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'phone_number', 'subject', 'message', 'seen',)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at',)