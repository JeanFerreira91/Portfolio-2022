from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'BlogApp'

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<category>/', views.blog_category_index, name='blog_category_index'),
    path('category/<category>/', views.blog_category_detail, name='blog_category_detail'),
]

urlpatterns += staticfiles_urlpatterns()