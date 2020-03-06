from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse
from django.utils.safestring import mark_safe
# Create your views here.
from django.core.handlers.wsgi import WSGIRequest
from utils import pagination


def index(request):
    v = reverse('author:index')
    print(type(request))
    print(request.environ)
    for k,v in request.environ.items():
        print(k,v)
    print(request.environ['HTTP_USER_AGENT'])
    return HttpResponse('ok')

def tpl1(request):
    user_list = [1,2,3,4]
    return render(request,'tpl1.html',{'u':user_list})

def tpl2(request):
    name = 'root'
    return render(request,'tpl2.html',{'name':name})

def tpl3(request):
    status = "已经删除"
    return render(request,'tpl3.html',{'status':status})

def tpl4(request):
    name = "IJIJIOJIJI"
    return render(request,'tpl4.html',{'name':name})

li = []
for i in range(1000):    #可以从数据中存储
    li.append(i)

def user_list(request):
    current_page = request.GET.get('p',1)
    current_page = int(current_page)
    val = request.COOKIES.get('per_page_count',10)
    val = int(val)
    page_obj = pagination.Page(current_page,len(li),val)
    data = li[page_obj.start():page_obj.end()]
    data = li[0:3]
    page_str = page_obj.page_str('/user_list/')
    return render(request,'user_list.html',{'u':data,'page_str':page_str})

user_info = {
    'dachengzi':{'pwd':'123123'},
    'kanbazi':{'pwd':'kkkkk'},
}

def auth(func):
    def inner(request,*args,**kwargs):
        v = request.COOKIES.get("username")
        if not v:
            return redirect('/login/')
        return func(request,*args,**kwargs)
    return inner

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('pwd')
        dic = user_info.get(u)
        if not dic:
            return render(request,'login.html')
        if dic['pwd'] == p:
            res = redirect('/index/')
            res.set_cookie('username',u,max_age=10)
            res.set_cookie('pwe','adadadasd',httponly=True)
            return res   #返回给客户端 浏览器的东西
        else:
            return render(request,'login.html')

@auth
def index(request):
    v = request.COOKIES.get('username')
    return render(request,'index.html',{'current_user':v})

def cookie(request):
    pass

from django import views
from django.utils.decorators import method_decorator


class Order(views.View):
    @method_decorator(auth)
    def dispatch(self, request, *args, **kwargs):
        return super(Order,self).dispatch(request,*args,**kwargs)

    def get(self,request):
        v = request.COOKIES.get('username')
        return render(request,'index.html',{'current_user':v})
    def post(self,request):
        v = request.COOKIES.get('username')
        return render(request,'index.html',{'current_user':v})

def order(request):
    v = request.COOKIES.get("username")
    return render(request,'index.html',{'current_user':v})