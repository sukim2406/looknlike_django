from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='proejct', null=True)
    title = models.CharField(max_length=150, null=False)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to='projects/', null=False)
    created_at = models.DateField(auto_now=True)