from django.contrib import admin
from .models import Category,Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display = ("title","category__category_name","author","status","is_featured","updated_at")
    search_fields = ("id","title","status","author")
    list_editable = ("status","is_featured")

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog,BlogAdmin)