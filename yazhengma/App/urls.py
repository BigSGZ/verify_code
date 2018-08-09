# encoding: utf-8
from django.conf.urls import url

from App import views

urlpatterns=[
    url(r'getverifcode',views.get_verify_code,name='get_verif_code'),
    url(r'^userlogin/',views.user_login,name='user_login')
]
