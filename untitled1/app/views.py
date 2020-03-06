from django.shortcuts import render
from app import models
from django import forms
from django.forms import widgets
from django.forms import fields
# Create your views here.

class Fm(forms.Form):
    user = fields.CharField(error_messages={'required':'用户名不能为空'},
                           widget=widgets.TextInput(attrs={'class':'sty'}),
                            show_hidden_initial=True,
                            help_text='名字'
                           )
    pwd = fields.CharField(max_length=12,min_length=4,error_messages={'required':'密码不能为空','max_length':'密码长度过长','min_length':'密码长度太短'})
    email = fields.EmailField(error_messages={'invalid':"邮箱格式错误",'required':'邮箱不能为空'})
    file = fields.FileField

def verify(request):
    if request.method == 'GET':
        obj = Fm()
        return render(request,"verify.html",{'obj':obj})
    elif request.method == 'POST':
        print(request.POST)
        print('--------')
        obj = Fm(request.POST)
        print(obj)
        a = obj.is_valid()
        if a:
            print(obj.cleaned_data)
            models.UserInfo.objects.create(**obj.cleaned_data)
        else:
            print(obj.errors)
            return render(request,"verify.html",{'obj':obj})

        return render(request,"verify.html")