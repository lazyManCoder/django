from django.db import models

# Create your models here.

class Category(models.Model):
    caption = models.CharField(max_length=32)

# class ArticleType(models.Model):
#     caption = models.CharField(max_length=32)

class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=255)
    category = models.ForeignKey("Category",on_delete=True)
    type_choice = (
    (1,'python'),
    (2,'linux'),
    (3,'openstack'),
    )
    article_type_id = models.IntegerField(choices=type_choice)

class UserInfo(models.Model):
    user = models.CharField(max_length=32,null=True)
    pwd = models.CharField(max_length=32,null=True)
    email = models.EmailField(max_length=32,null=True)