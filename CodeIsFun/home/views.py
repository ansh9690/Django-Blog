from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from blog.models import Post


def home(request):
    blog = Post.objects.all().order_by('-timeStamp')[0:5]

    context = {
        'post': blog
    }
    return render(request, 'home/home.html', context)


def contact(request):
    if request.method == 'POST':
        if request.POST['name1'] == '' and request.POST['email'] == '' and request.POST['phone'] == '':
            messages.info(request, "Please provide information")
        else:
            contact = Contact(name=request.POST['name1'], email=request.POST['email'],
                              phone=request.POST['phone'], content=request.POST['content'])
            contact.save()
            messages.success(request, "Your form submitted, We will reach you soon")
    return render(request, 'home/contact.html')


def search(request):
    query = request.GET['query']
    if len(query) > 50:
        search_all = Post.objects.none()
    else:
        search_post = Post.objects.filter(title__icontains=query)
        search_content = Post.objects.filter(content__icontains=query)
        search_all = search_post.union(search_content)
    if search_all.count() == 0:
        messages.warning(request, "Search results not found..!")
    else:
        messages.info(request, "Results...")
    context = {
        'post': search_all,
        'query': query
    }
    return render(request, 'home/search.html', context)


