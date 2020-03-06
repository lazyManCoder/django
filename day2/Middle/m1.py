from django.utils.deprecation import MiddlewareMixin

class Row1(MiddlewareMixin):
    def process_request(self,request):
        print('hello')

    def process_view(self,request,view_func,view_func_args,view_func_kwargs):
        print('zhang')

    def process_response(self,request,response):
        print('hou')
        return response

class Row2(MiddlewareMixin):
    def process_request(self,request):
        print('hello2')

    def process_view(self,request,view_func,view_func_args,view_func_kwargs):
        print('zhang2')

    def process_response(self,request,response):
        print('hou2')
        return response


class Row3(MiddlewareMixin):
    def process_request(self,request):
        print('hello3')

    def process_view(self,request,view_func,view_func_args,view_func_kwargs):
        print('zhang3')

    def process_response(self,request,response):
        print('hou3')
        return response
