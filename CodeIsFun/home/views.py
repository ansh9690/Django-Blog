from django.shortcuts import render, HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post


def home(request):
    return render(request, 'home/home.html')


def contact(request):
    if request.method == 'POST':
        if request.POST['name1'] == '' and request.POST['email'] == '' and request.POST['phone'] == '':
            messages.info(request, "Please Provide information")
        else:
            contact = Contact(name=request.POST['name1'], email=request.POST['email'],
                              phone=request.POST['phone'], content=request.POST['content'])
            contact.save()
            messages.success(request, "Your form submitted, We will reach you soon")
    return render(request, 'home/home.html')


def search(request):
    query = request.GET['query']
    if len(query) > 50:
        search_post = Post.objects.none()
    else:
        search_post = Post.objects.filter(title__icontains=query)
    context = {
        'post': search_post,
        'query': query
    }
    return render(request, 'home/search.html', context)


def post(request):
    post1 = Post.objects.last()
    context = {
        'post': post1
    }
    return render(request, 'blog/post.html', context)


