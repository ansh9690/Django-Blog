from django.shortcuts import render, HttpResponse, redirect
from .models import Post, BlogComment


def index(request):
    blog = Post.objects.all()
    context = {
        'post': blog
    }
    return render(request, 'blog/index.html', context)


def post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(postcomment=post)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'blog/post.html', context)

def comments(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        postId = request.POST.get('postId')
        postcomment = Post.objects.get(sno=postId)
        user = request.user

        comment = BlogComment(comment=comment, user=user, postcomment=postcomment)
        comment.save()

    return redirect("/")
