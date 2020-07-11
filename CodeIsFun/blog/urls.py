from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/my-all-post/', views.MyPost, name='my_post'),
    path('post/<int:pk>/delete/', views.DeletePost, name='delete_post'),
    path('post/new/', views.CreatePost, name='create_post'),
    path('post/<int:pk>/update/', views.UpdatePost, name='update'),
    path('post/postComment/', views.postComment, name='postComment'),
    path('post/postComment/<int:pk>/delete/', views.deleteComment, name='delete_comment'),
    path('post/', views.index, name='index'),
    path('post/<int:pk>/', views.post, name='post'),

]

