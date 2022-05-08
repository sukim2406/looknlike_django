from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='posts/', null=False)
    created_at = models.DateField(auto_now_add=True)