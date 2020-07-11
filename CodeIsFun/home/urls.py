from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/contact-us/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
]
