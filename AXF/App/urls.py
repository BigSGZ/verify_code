# encoding: utf-8
from django.conf.urls import url

from App import views

urlpatterns=[
    url(r'^hello/',views.hello),
    url(r'^home/',views.home,name='home'),
    url(r'^mine/',views.mine,name='mine'),
    url(r'^market/',views.market,name='market'),
    url(r'^cart/',views.cart,name='cart'),
    url(r'^market_with_parmas/(?P<categoryid>\d+)/(?P<childcid>\d+)/(?P<order_rule>\d+)/',views.market_with_parmas,name='market_with_parmas'),
    url(r'^userregister/',views.user_register,name='user_register'),
    url(r'^userlogout/',views.user_logout,name='user_logout'),
    url(r'^checkuser/',views.check_user,name='checkuser'),
    url(r'^checkemail/',views.check_email,name='checkemail'),
    url(r'^userlogin/',views.user_login,name='user_login'),
    url(r'^sendmail/',views.send_email_learn),
    url(r'^activateuser/',views.activateuser),
    url(r'^addtocart/',views.addtocart,name='addtocart')
]
