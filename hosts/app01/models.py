from django.db import models

# Create your models here.

class Business(models.Model):
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32,null=True,default='SA')


class Host(models.Model):
    uid = models.AutoField(primary_key=True)   #自增
    hostname = models.CharField(max_length=32,db_index=True)  #字符型
    ip = models.GenericIPAddressField(protocol='both',db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey("Business",on_delete=models.CASCADE)


class Application(models.Model):
    name = models.CharField(max_length=32,null=True)
    r = models.ManyToManyField("Host")

# class Application(models.Model):
#     name = models.CharField(max_length=32,null=True)

# class HostToApp(models.Model):
#     hobj = models.ForeignKey("Host",on_delete=models.CASCADE,null=True)
#     aobj = models.ForeignKey("Application",on_delete=models.CASCADE,null=True)
    






