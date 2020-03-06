from django.shortcuts import render
from app import models
from django.urls import reverse
# Create your views here.


def article(request,*args,**kwargs):
    # print(request.path_info)
    # url = reverse('article',kwargs={'article'})
    container = {}
    for k,v in kwargs.items():
        if v == '0':
            pass
        else:
            container[k] = v
    article_type_list = models.ArticalType.objects.all()
    category_list = models.Category.objects.all()
    content = models.Article.objects.filter(**container)
    return render(request,"artical.html",{'content':content,'article_type':article_type_list,'category':category_list,'arg_list':kwargs})