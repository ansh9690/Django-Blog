from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact-us/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
]
