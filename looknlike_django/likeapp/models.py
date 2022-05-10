from django.db import models
from django.contrib.auth.models import User
from postapp.models import Post

# Create your models here.

class LikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='like_record', null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes_record')

    class Meta:
        unique_together = ('user', 'post')
        