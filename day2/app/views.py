from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    elif request.method == "POST":
        u = request.POST.get("user")
        p = request.POST.get("pwd")
        if u == "root" and p == "123":
            request.session['username'] = u
            request.session['is_login'] = True
            if request.POST.get('rmb',None) == '1':
                request.session.set_expiry(3)
            return redirect('/index/')
        else:
            return render(request,"login.html")

def index(request):
    if request.session.get('is_login'):
        return render(request,"index.html",{"username":request.session['username']})
    else:
        return render(request,"login.html")

def logout(request):
    request.session.clear()
    return redirect('/login/')


def test(request,nid):
    print('who are you !')
    return HttpResponse('ok')

from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def cache(request):
    import time
    ctime = time.time()
    return render(request,'cache.html',{'ctime':ctime})

from django import forms
from django.forms import widgets  #所有的插件
from django.forms import fields   #所有的字段
class FM(forms.Form):
    user = fields.CharField(widget=widgets.Textarea({"class":'c1'}),
                            label="用户名",

                            )
    pwd = fields.CharField(max_length=12,min_length=6,error_messages={'min_length':'密码长度不能小于6','max_length':'密码长度不能大于12'},
                           widget=widgets.PasswordInput({"class":"c2"}))  #可以自定义样式
    email = fields.EmailField()

    p = fields.FilePathField(path='app')

    city1 = fields.ChoiceField(
        choices=[(0,'上海'),(1,'广州'),(2,'深圳')]
    )

    city2 = fields.MultipleChoiceField(
        choices=[(0,'上海'),(1,'广州'),(2,'深圳')]
    )
from app import models
def fm(request):
    if request.method == "GET":
        #从数据库中把数据获取
        dic = {
            "user":"r1",
            "pwd":'123123',
            "email":'sadad',
            "city1":1,
            "city2":[1,2]
        }

        obj = FM(initial=dic)
        return render(request,"fm.html",{'obj':obj})
    elif request.method == "POST":
        obj = FM(request.POST)
        r1 = obj.is_valid()
        if r1:
            #print(obj.cleaned_data)  #输出正确的数据  接收
            models.UserInfo.objects.create(**obj.cleaned_data)
        else:
            print(obj.errors)
            return render(request,'fm.html',{"obj":obj})
        return render(request,"fm.html")