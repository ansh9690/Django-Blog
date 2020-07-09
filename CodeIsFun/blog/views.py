from django.shortcuts import render, HttpResponse, redirect
from .models import Post, BlogComment
from django.contrib import messages
from blog.templatetags import extras


def index(request):
    blog = Post.objects.all()
    context = {
        'post': blog
    }
    return render(request, 'blog/index.html', context)


def post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    reply_dict = {}
    for reply in replies:
        if reply.parent.sno not in reply_dict.keys():
            reply_dict[reply.parent.sno] = [reply]
        else:
            reply_dict[reply.parent.sno].append(reply)
    context = {
        'post': post,
        'comments': comments,
        'user': request.user,
        'replyDict': reply_dict,
    }
    return render(request, 'blog/post.html', context)


def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        post_sno = request.POST.get('post_sno')
        post_comment = Post.objects.get(sno=post_sno)
        parent_sno = request.POST.get('parent_sno')
        if parent_sno == "":
            comment = BlogComment(comment=comment, user=user, post=post_comment)
            comment.save()
            messages.success(request, "Successfully posted comment")
        else:
            parent = BlogComment.objects.get(sno=parent_sno)
            comment = BlogComment(comment=comment, user=user, post=post_comment, parent=parent)
            comment.save()
            messages.success(request, "Successfully posted reply comment")
    return redirect(f"/blog/{post_comment.slug}")
