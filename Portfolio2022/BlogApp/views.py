from django.http import Http404
from django.shortcuts import  get_object_or_404, render

from .models import BlogPost

# Create your views here.
def blogView(request):
    latest_post_list = BlogPost.objects.order_by('-pub_date')[:5]
    context = {
        'latest_post_list': latest_post_list,
    }
    return render(request, 'BlogApp/blog_index.html', context)

def blogDetail(request, blog_id):
    blog_post = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, 'BlogApp/blog_detail.html', {'blog_post': blog_post})