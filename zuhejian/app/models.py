from django.db import models

# Create your models here.

class Category(models.Model):
    caption = models.CharField(max_length=32)

class ArticalType(models.Model):
    caption = models.CharField(max_length=32)

class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=255)
    category = models.ForeignKey("Category",on_delete=True)
    artical_type = models.ForeignKey("ArticalType",on_delete=True)
