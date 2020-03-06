from django.shortcuts import render

# Create your views here.
from django import forms
from app import models
from django.forms import fields
from django.forms import widgets as w

class UserInfoModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = '__all__'
        labels = {
            'pwd':'密码',
            'email':'邮箱',
            'b':'分组',
        }

        widgets = {
            'username':w.Textarea(attrs={'class':'c1'})
        }

        error_message = {   #后台错误信息  在前端进行提示
            'email':{
                'required':'邮箱不能为空',
            }
        }

        # field_classes = {
        #     'email':fields.URLFIELD   #只能加类  不能加对象
        #
        # }


def index(request):
    if request.method == 'GET':
        obj = UserInfoModelForm()
        return render(request,'index.html',{'obj':obj})
    elif request.method == 'POST':
        obj = UserInfoModelForm(request.POST)
        if obj.valid():
            obj.save()   #帮我们自己保存 表   拆分
            # instance = obj.save(False)
            # instance.save()
            # obj.save_m2m()   等价的关系
        print(obj.is_valid())
        print(obj.cleaned_data)
        return render(request,'index.html',{'obj':obj})

def user_list(request):
    li = models.UserInfo.objects.all().select_related("user_type")
    return render(request,"user_list.html",{'li':li})