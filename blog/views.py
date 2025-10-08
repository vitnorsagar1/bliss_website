# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'blogs': blogs})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/blog_detail.html', {'blog': blog})
