from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
def login(request):
    error_message = " "
    if request.method == "POST":
        v = request.POST.get('gender',None)
        print(v)
        user = request.POST.get('u',None)
        pwd = request.POST.get('q',None)
        e = request.POST.get('e',None)

        file = request.FILES.get('fafa',None)
        print(type(file))

        # if user == "root" and pwd == "123":
        #     return render(request,'home.html')
        # else:
        #     error_message = "error try again"

        res = models.UserInfo.objects.filter(username=user,password=pwd,email=e).first() #返回的是一个对象
        if res:
            # return render(request,'home.html')
            return redirect('/cmdb/index')
        else:
            error_message = "error try again"

    return render(request,'login.html',{"error":error_message})


USER_LIST = [
    {'username':'alex','age':23,'gender':'男'}
]
# for i in range(20):
#     temp = {'username':'alex'+str(i),'age':23,'gender':'男'}
#     USER_LIST.append(temp)

def home(request):
    if request.method == "POST":
        user = request.POST.get('username',None)
        age = request.POST.get('age',None)
        gender = request.POST.get('gender',None)
        tmp = {'username':user,'age':age,'gender':gender}
        USER_LIST.append(tmp)
    return render(request,'home.html',{'user_list':USER_LIST})



USER_DICT = {
    'root1':'root@live',
    'root2':'root@live',
    'root3':'root@live',
    'root4':'root@live',
    'root5':'root@live',
}
def index(request):
    return render(request,'index.html',{'user_dict':USER_DICT})

# def detail(request,nid):
#     # return render(request,'detail.htm1l',{'user_dict':USER_DICT})
#     return HttpResponse('<h1>'+str(nid)+'</h>')

from cmdb import models
# def orm(request):
#     models.UserInfo.objects.create(
#         username = 'root',
#         password = '123',
#         email = '12344'
#     )
#
#     # all = models.UserInfo.objects.all()
#     # for row in all:
#     #     print(row.id,row.username,row.password,row.email)
#
#     select = models.UserInfo.objects.filter(id=4)
#     for row in select:
#         print(row.id,row.username,row.password,row.email)
#
#     # deleta = models.UserInfo.objects.filter(id=2).delete()
#     # print(deleta)
#
#     update = models.UserInfo.objects.filter(id=3).update(password=123)   #更新数据
#     return HttpResponse('orm')

# def orm(request):
#     if request.method == "POST":
#         u = request.POST.get('user',None)
#         p = request.POST.get('pwd',None)
#         e = request.POST.get('email',None)
#         models.UserInfo.objects.create(username=u,password=p,email=e)
#     return render(request,'user_info.html')

def user_info(request):
    if request.method == 'POST':
        u = request.POST.get('u',None)
        p = request.POST.get('p',None)
        e = request.POST.get('e',None)
        print(u,p,e)
        models.UserInfo.objects.create(username=u,password=p,email=e)
        # userinfo = models.UserInfo.objects.all()
        # return render(request,'user_info.html',{'userinfo':userinfo})
        return redirect('/cmdb/user_info/')
        # return redirect("http://www.baidu.com")
    elif request.method == 'GET':
        userinfo = models.UserInfo.objects.all()
        user_list = models.UserGroup.objects.all()
        sel = request.Get.get('t2',None)

        return render(request,'user_info.html',{'userinfo':userinfo,'userlist':user_list})
    # elif request.method == 'POST':
    #     u = request.POST.get('u',None)
    #     p = request.POST.get('p',None)
    #     e = request.POST.get('e',None)
    #     print(u,p,e)
    #     models.UserInfo.objects.create(username=u,password=p,email=e)
    #     # userinfo = models.UserInfo.objects.all()
    #     # return render(request,'user_info.html',{'userinfo':userinfo})
    #     return redirect('/cmdb/user_info/')

def user_group(request):
    return render(request,'user_group.html')


def user_detail(request,nid):
    obj = models.UserInfo.objects.filter(id=nid).first()

    return render(request,'user_detail.html',{'obj':obj})

def userdel(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/cmdb/user_info')

def user_edit(request,nid):
    if request.method == "POST":
        user = request.POST.get('user',None)
        pwd = request.POST.get('pwd',None)
        email = request.POST.get('e',None)
        new_dict = {'username':user,'password':pwd,'email':email}
        # id=nid).update(username=user,password=pwd,email=email
        models.UserInfo.objects.filter(**new_dict)
        # return redirect('/cmdb/user_info/')
        return redirect('/cmdb/user_info/')
    elif request.method == "GET":
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request,'user_edit.html',{'obj':obj})


def user_try(request):
    models.UserGroup.objects.create(uid='1',caption='hello')
    obj = models.UserGroup.objects.filter(uid=1).first()
    obj.caption = "CEO"
    obj.save()

    return HttpResponse('user_try')
