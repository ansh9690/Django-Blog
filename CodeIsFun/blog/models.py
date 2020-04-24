from django.db import models


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    content = models.TextField()
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title
