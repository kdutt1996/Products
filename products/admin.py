from django.contrib import admin
from .models import Product, Category, Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_filter = ("category", "tags")
    search_fields = ("name", "description")
    filter_horizontal = ("tags",)
