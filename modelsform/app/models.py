from django.db import models

# Create your models here.

class UserType(models.Model):
    caption = models.CharField(max_length=32)

class UserGroup(models.Model):
    name = models.CharField(max_length=32)

class UserInfo(models.Model):
    username = models.CharField(verbose_name="用户名",max_length=32)
    pwd = models.CharField(max_length=32)
    email = models.EmailField()
    b = models.ForeignKey("UserType",on_delete=True)
    u2g = models.ManyToManyField(UserGroup)