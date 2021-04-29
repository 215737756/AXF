# -- coding: utf-8 --
from django.conf.urls import url

from Axfuser import views

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^checkname/', views.checkName, name='checkname'),
    url(r'^matchpassword/', views.matchpassword, name='matchpassword'),
    # 测试 Email
    url(r'^testemail/', views.testemail, name='testemail'),
]
