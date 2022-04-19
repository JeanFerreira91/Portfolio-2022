from django.urls import path

from . import views

app_name = 'BlogApp'

urlpatterns = [
    path('', views.blogView, name='blog'),
    path('<int:blog_id>/', views.blogDetail, name='blog_detail'),
]