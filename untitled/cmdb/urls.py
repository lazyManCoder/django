from django.contrib import admin
from django.urls import path,re_path
from cmdb import views

urlpatterns = [

    path('login/', views.login),
    path('home/', views.home),
    path('index/', views.index),
    # re_path('detail-(?P<nid>\d+).html/', views.detail,name="detail"),
    # path('orm/',views.orm),
    path('user_info/',views.user_info),
    path('user_group/',views.user_group),
    path('user_try/',views.user_try),
    re_path('userdetail-(\d+)/',views.user_detail),
    re_path('userdel-(\d+)/',views.userdel),
    re_path('useredit-(\d+)/',views.user_edit,name="edit"),


]
