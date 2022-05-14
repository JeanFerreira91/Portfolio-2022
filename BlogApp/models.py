import datetime
from distutils.command.upload import upload
from tabnanny import verbose

from django.db import models
from django.db.models import Model
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    # Customising the Admin Page
    class Meta:
        verbose_name_plural = 'Categories'


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(default='', upload_to='BlogApp/static')
    body = RichTextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name='posts')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:280]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    
    def was_published_recently(self):
        now = datetime.timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    # Customising the Admin Page
    class Meta:
        verbose_name_plural = 'Blog Posts'


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("BlogPost", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.body[:60]
    
    # Customising the Admin Page
    class Meta:
        verbose_name_plural = 'Users Comments'