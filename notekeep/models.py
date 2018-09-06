from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=8)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Note(models.Model):
    title = models.CharField(max_length=1000)
    body = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
