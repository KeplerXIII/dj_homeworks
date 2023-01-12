from django.contrib import admin

from .models import Article, Scope, Tag


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 2

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

