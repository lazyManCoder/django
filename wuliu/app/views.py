from django.shortcuts import render,redirect,HttpResponse
# Create your views here.
from django import forms
from django.forms import widgets
from django.forms import fields
from app import models
from utils import pagination

class FM(forms.Form):
    user = fields.CharField(label="账 户:")
    pwd = fields.CharField(widget=widgets.PasswordInput,label="密 码:",max_length=12,min_length=6,error_messages={'min_length':'密码长度不小于6','max_length':'密码长度不大于12'})

def login(request):
    if request.method == 'GET':
        obj = FM()
        return render(request,"login.html",{'obj':obj})
    elif request.method == 'POST':
        obj = FM(request.POST)
        global user
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        u = models.UserInfo.objects.filter(user=user)
        p = models.UserInfo.objects.filter(pwd=pwd)
        if u and p:
            res = redirect('/cmdb/index/')
            res.set_cookie('username',u)
            request.session['user'] = user
            request.session['is_login'] = True
            return res
        return render(request,'login.html',{'obj':obj})

def auth(func):
    def inner(request,*args,**kwargs):
        v = request.session.get('is_login')
        if not v:
            return redirect('/login/')
        return func(request,*args,**kwargs)
    return inner

li = []
for i in range(100):
    li.append(i)

@auth
def index(request):
    current_page = request.GET.get('p',1)
    current_page = int(current_page)
    page_obj = pagination.Page(current_page,len(li))
    data = li[0:3]
    page_str = page_obj.page_str('/cmdb/index/')
    return render(request,"index.html",{'u':user,'page_str':page_str,'v':data})


def zhuce(request):
    if request.method == 'GET':
        return render(request,"zhuce.html")
    elif request.method == 'POST':
        obj = FM(request.POST)
        r1 = obj.is_valid()
        if r1:
            models.UserInfo.objects.create(**obj.cleaned_data)
        else:
            return render(request,"zhuce.html",{'obj':obj})
    return render(request,"login.html")

def logout(request):
    request.session.clear()
    return redirect('/cmdb/login/')

def test(request):
    current_page = request.GET.get('p',1)
    current_page = int(current_page)
    page_obj = pagination.Page(current_page,len(li))
    data = li[0:3]
    page_str = page_obj.page_str('/cmdb/index/')
    return render(request,"test.html",{'page_str':page_str})

def mine(request):
    return render(request,"mine.html")