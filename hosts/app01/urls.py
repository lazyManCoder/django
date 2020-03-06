from django.contrib import admin
from django.urls import path,include,re_path
from app01 import views
urlpatterns = [
    path('host/',views.host),
    re_path('business/$',views.business),
    re_path('host/$',views.host),
    re_path('test_ajax/$',views.test_ajax),
    re_path('app/$',views.app),
    re_path('ajax_add_app/$',views.ajax_add_app),
]