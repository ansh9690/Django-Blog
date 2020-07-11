from django.shortcuts import render, redirect, get_object_or_404, HttpResponse, HttpResponseRedirect
from .models import Post, BlogComment, PostForm, UpdatePostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    blog = Post.objects.all()
    context = {
        'post': blog
    }
    return render(request, 'blog/index.html', context)


def post(request, pk):
    post = Post.objects.filter(pk=pk).first()
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


@login_required(login_url='account:login')
def MyPost(request):
    my_post = Post.objects.filter(author_name=request.user)
    context = {
        'post': my_post
    }
    return render(request, 'blog/mypost.html', context)


@login_required(login_url='account:login')
def DeletePost(request, pk):
    delete_post = Post.objects.get(pk=pk)
    if request.user == delete_post.author_name:
        delete_post.delete()
        messages.success(request, "Deleted Post")
        return redirect('blog:my_post')


@login_required(login_url='account:login')
def CreatePost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author_name = request.user
            instance.save()
            messages.success(request, "Posted Successfully Article")
            return redirect('blog:post', instance.sno)
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request, 'blog/new_post.html', context)


@login_required(login_url='account:login')
def UpdatePost(request, pk):
    update_post = Post.objects.get(pk=pk)
    if request.user == update_post.author_name:
        if request.method == 'POST':
            form = UpdatePostForm(request.POST, instance=update_post)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author_name = request.user
                instance.save()
                messages.success(request, "Posted Successfully Updated Article")
                return redirect('blog:post', instance.sno)
        else:
            form = UpdatePostForm(instance=update_post)
        context = {
            'form': form
        }
        return render(request, 'blog/update_post.html', context)
    else:
        return HttpResponse("Invalid")


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
    return redirect(f"/blog/post/{post_comment.pk}")


@login_required(login_url='account:login')
def deleteComment(request, pk):
    delete_comments = get_object_or_404(BlogComment, pk=pk)
    if request.user == delete_comments.user:
        delete_comments.delete()
        messages.success(request, "Deleted Successfully")
        return redirect(request.META['HTTP_REFERER'])

