from django.shortcuts import render

# Create your views here.


def article(request,nid):
    print(nid)
    return render(request,"article.html")