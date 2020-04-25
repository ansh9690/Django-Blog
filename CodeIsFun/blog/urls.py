from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('addcomment/', views.comments, name='comment'),
    path('', views.index, name='index'),
    path('<str:slug>/', views.post, name='post'),
]
