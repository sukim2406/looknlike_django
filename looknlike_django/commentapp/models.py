from django.db import models
from postapp.models import Post
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)