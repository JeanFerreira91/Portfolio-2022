from django.contrib import admin
from BlogApp.models import BlogPost, BlogPostRich, Category, Comment

# Register your models here.
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'last_modified']
    ordering = ['-pub_date']
    
class BlogPostRichAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'last_modified']
    ordering = ['-pub_date']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'body', 'created_on']
    ordering = ['-created_on']
    
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogPostRich, BlogPostRichAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, BlogCommentAdmin)
# admin.site.header = 'JeanPy BlogApp Admin'
# admin.site.site_title = 'JeanPy BlogApp Admin'
# admin.site.index_title = 'Django Admin for JeanPy Blog'