from django.http import Http404
from django.shortcuts import  get_object_or_404, render

from .models import *
from BlogApp.forms import CommentForm

# Create your views here.
def blog_index(request):
    latest_posts_list = BlogPost.objects.order_by('-pub_date')[:5]
    context = {
        'latest_posts_list': latest_posts_list,
    }
    return render(request, 'BlogApp/blog_index.html', context)


def blog_category(request, category):
    posts = BlogPost.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'BlogApp/blog_category.html', context)


def blog_detail(request, pk):
    post = BlogPost.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data['author'],
                body = form.cleaned_data['body'],
                post = post
            )
            comment.save()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'BlogApp/blog_detail.html', context)
