from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    content = models.TextField()
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    postcomment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parentcomment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    addedTime = models.DateTimeField(auto_now_add=True)
