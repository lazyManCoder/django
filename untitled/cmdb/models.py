from django.db import models

# Create your models here.

class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)  #自增键
    caption = models.CharField(max_length=32)
    ctime = models.DateTimeField(auto_now_add=True,null=True)



class UserInfo(models.Model):
    #自增id键
    username = models.CharField(max_length=32,blank=True,verbose_name='用户名')
    password = models.CharField(max_length=64,error_messages={'required':'请输入密码:'},help_text='pwd')
    email = models.CharField(max_length=32,null=True)
    user_group = models.ForeignKey('UserGroup',on_delete=models.CASCADE,null=True,default=1)
    user_type_choice = (
            (1,'超级用户'),
            (2,'普通用户'),
            (3,'噗噗噗用户'),
    )

    user_type_id = models.IntegerField(choices=user_type_choice,default=1)

