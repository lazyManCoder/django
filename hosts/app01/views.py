from django.shortcuts import render,redirect,HttpResponse
import json
# Create your views here.
from app01 import models
def host(request):
    if request.method == 'GET':
        v = models.Host.objects.all()
        b_list = models.Business.objects.all()
        # a = models.Host.objects.filter(uid__gt=0).values('hostname','b__caption')  通过双下滑线进行跨表
        # print(a)
        return render(request,'host.html',{'v':v,'b_list':b_list})
    elif request.method == 'POST':
        hostname = request.POST.get('hostname',None)
        ip = request.POST.get('ip',None)
        port = request.POST.get('port',None)
        b = request.POST.get('b_id',None)
        print(hostname,ip,port,b)
        models.Host.objects.create(hostname=hostname,ip=ip,port=port,b_id = b)  #b_id也可以写成，b = models.Host.filter(id=b)
        return redirect('/app01/host/')

def business(request):
    v = models.Business.objects.all()
    a = models.Business.objects.values('caption','code')
    h = models.Business.objects.values_list('caption','code')
    return render(request,'business.html',{'v':v,'a':a,'h':h})

def test_ajax(request):
    ret = {'status':True,'error':None,'data':None}
    try:
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        if h and len(h) > 3:
            models.Host.objects.create(hostname=h,ip=i,port=p,b_id=b)
        else:
            ret['status'] = False
            ret['error'] = 'to short !'
    except Exception as e:
        ret['status'] = False
        ret['data'] = '请求错误'

    return HttpResponse(json.dumps(ret))


def app(request):
    if request.method == 'GET':
        app_list = models.Application.objects.all()
        host_list = models.Host.objects.all()
        return render(request,'app.html',{'app_list':app_list,'host_list':host_list})
    elif request.method == 'POST':
        app_name = request.POST.get('app_name')
        host_list = request.POST.getlist('host_list')
        print(app_name,host_list)
        obj = models.Application.objects.create(name=app_name)
        obj.r.add(*host_list)  #跨表进行添加
        return redirect('/app01/app/')


def ajax_add_app(request):
    ret = {'status':True, 'error':None, 'data': None}
    app_name = request.POST.get('app_name')
    host_list = request.POST.getlist('host_list')
    obj = models.Application.objects.create(name=app_name)
    obj.r.add(*host_list)
    return HttpResponse(json.dumps(ret))



