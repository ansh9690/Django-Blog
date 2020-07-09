from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User


def home(request):
    return render(request, 'account/home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=request.POST['email']).exists():
                messages.info(request, "Email already taken")
            else:
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f"Account Created {username}")
                return redirect('account:login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})