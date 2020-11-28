from django.contrib import admin
from .models import Author, Category, Post
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    
admin.site.register(Author, AuthorAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    
admin.site.register(Category, CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'post_author', 'post_date']
    
    
admin.site.register(Post, PostAdmin)