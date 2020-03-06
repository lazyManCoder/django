from django.contrib import admin
from django.urls import path,re_path
from app import views
from django.conf.urls import url,include
app_name = 'app'
urlpatterns = [

    path('index/',views.index,name="index"),

]