from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils import timezone
from tinymce.models import HTMLField


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    content = HTMLField()
    author_name = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    timeStamp = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title[0:20]


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content']


class UpdatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content']


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[0:15] + "..." + "by " + self.user.username
