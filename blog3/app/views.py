from django.shortcuts import render,HttpResponse
from app import models
import requests
from io import BytesIO
from PIL import ImageFont
from utils.check_code import ValidCodeImg
# Create your views here.
def article(request,*args,**kwargs):
    print('-----------------',kwargs)
    container = {}
    for k,v in kwargs.items():
        kwargs[k] = int(v)
        if v == '0':
            pass
        else:
            container[k] = v
    article_type_list = models.Article.type_choice
    print(article_type_list)

    category_list = models.Category.objects.all()
    contents = models.Article.objects.filter(**container)
    return render(request,"article.html",{'content':contents,'article_type':article_type_list,'category':category_list,'arg_list':kwargs})

def jsonp(request):
    print(request.GET)
    name = request.GET.get('callback')
    print(name)
    content = '%s(100)'%(name,)
    return HttpResponse(content)


def images(request):
    response = requests.get('https://api.jisuapi.com/weather/query?callback=list&appkey=e5de5fcbe1800420&city=%E5%AE%BF%E5%B7%9E')
    response.encode = 'utf-8'
    return render(request,'jsonp.html',{'res':response.text})

def kind(request):
    return render(request,'kind.html')





def check_code(request):
    img = ValidCodeImg()
    data, valid_str = img.getValidCodeImg()
    print(valid_str)
    request.session['check'] = valid_str
    return HttpResponse(data,valid_str)

def login(request):
    if request.method == 'POST':
        check = request.POST.get('check')
        print(check)
        if check.upper() == request.session['check']:
            print('验证通过')
        else:
            print('验证失败')
    return render(request,"login.html")

def verify(request):
    return