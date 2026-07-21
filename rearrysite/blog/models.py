from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=1024)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)