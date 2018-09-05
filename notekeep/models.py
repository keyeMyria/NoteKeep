from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=1000)
    body = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)