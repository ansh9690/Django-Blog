from django.shortcuts import render, HttpResponse
from .models import Post


def index(request):
    blog = Post.objects.all()
    context = {
        'post': blog
    }
    return render(request, 'blog/index.html', context)


def post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context)
