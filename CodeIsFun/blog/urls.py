from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('postComment/', views.postComment, name='postComment'),
    path('', views.index, name='index'),
    path('<str:slug>/', views.post, name='post'),
]


