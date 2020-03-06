from django.shortcuts import render,redirect

# Create your views here.

def login(request):
    error_message = ""
    if request.method == "POST":
        user = request.POST.get('u',None)
        import os
        obj = request.FILES.get('faf')
        print(obj)
        file_path = os.path.join('upload',obj.name)
        print(file_path)
        f = open(file_path,mode="wb")
        for i in obj.chunks():
            f.write(i)
        f.close()

        pwd = request.POST.get('q',None)
        if user == "root" and pwd == "115603":
            return render(request,'home.html')

        else:
            error_message = "error"
    return render(request,'login.html',{'error':error_message})