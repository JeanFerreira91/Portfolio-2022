from django.contrib import admin
from BlogApp.models import BlogPost, Category, Comment

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'last_modified']
    ordering = ['-pub_date']
    search_fields = ['title__icontains', 'body__icontains']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name__icontains']
    
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'body', 'created_on']
    ordering = ['-created_on']
    search_fields = ['author__icontains', 'body__icontains']
    
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, BlogCommentAdmin)
# admin.site.header = 'JeanPy BlogApp Admin'
# admin.site.site_title = 'JeanPy BlogApp Admin'
# admin.site.index_title = 'Django Admin for JeanPy Blog'