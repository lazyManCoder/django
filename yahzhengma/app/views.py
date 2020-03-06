from django.shortcuts import render,HttpResponse
from utils.check_code import ValidCodeImg
# Create your views here.
def check(request):
    img = ValidCodeImg()
    data, valid_str = img.getValidCodeImg()
    print(valid_str)

    f = open('test.png', 'wb')
    f.write(data)
    f.close()
    return HttpResponse()
