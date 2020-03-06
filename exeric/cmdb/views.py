from django.shortcuts import render,HttpResponse

# Create your views here.

# def login(request):
#     if request.method == 'POST':
#         user = request.POST.get('user')
#         print(user)
#
#         a = request.POST.get('fafa',None)
#         print(type(a))
#     return render(request,'login.html')
from django.views import View
USER_LIST = {
    # 'k1':'root1',
    # 'k2':'root2',
    # 'k3':'root3',
    # 'k4':'root4',
    'k1':{'name':'root1','email':'root@live.com'},
    'k2':{'name':'root2','email':'root@live.com'},
    'k3':{'name':'root3','email':'root@live.com'},
    'k4':{'name':'root4','email':'root@live.com'},

}
def index(request):
    return render(request,'index.html',{'user_list':USER_LIST})


class login(View):
    def dispatch(self, request, *args, **kwargs):
        print("before")
        result = super(login,self).dispatch(request, *args, **kwargs)
        print("after")
        return result

    def get(self,request):
        print(request.method)
        return render(request,'home.html')

    def post(self,request):
        print(request.method)
        return render(request,'home.html')

def detail(request):
    nid = request.GET.get('nid')
    detail_info = USER_LIST[nid]
    return render(request,'detail.html',{'detail_info':detail_info})