from django.db import models
from django.contrib.auth.models import User
from projectapp.models import Project

# Create your models here.

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='posts/', null=False)
    created_at = models.DateField(auto_now_add=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='post', null=True)
    like = models.IntegerField(default=0)