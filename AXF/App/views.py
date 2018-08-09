# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.core.cache import cache
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse

from App.models import HomeWheel, HomeNav, HomeMustbuy, HomeShop, HomeMainShow, Foodtype, Goods, UserModel, CartModel

ALL_TYPE='0'
ORDER_TOTAL='0'
PRICE_ASC='1'
PRICE_DESC='2'
def hello(request):
    return HttpResponse('hello')
def home(request):
    wheels= HomeWheel.objects.all()
    navs=HomeNav.objects.all()
    mustbuys=HomeMustbuy.objects.all()
    shops=HomeShop.objects.all()
    shop0_1=shops[0:1]
    shops1_3=shops[1:3]
    shops3_7=shops[3:7]
    shops7_11=shops[7:11]
    mainshows=HomeMainShow.objects.all()
    data={
        'title':'首页',
        "wheels":wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shops':shops,
        'shop0_1':shop0_1,
        'shops1_3':shops1_3,
        'shops3_7':shops3_7,
        'shops7_11':shops7_11,
        'mainshows':mainshows
    }
    return render(request,'home/home.html',context=data)
def mine(request):

    is_login=False
    user_id=request.session.get('user_id')
    data = {
        'title': '我的',
        'is_login': is_login
    }
    if user_id:
        is_login=True
        user=UserModel.objects.get(pk=user_id)
        data['is_login']=is_login
        data['user_icon']= '/static/upload/'+ user.u_icon.url
        data['username']=user.u_name

    return render(request,'mine/mine.html',context=data)
def market(request):
   return  redirect(reverse('app:market_with_parmas',kwargs={'categoryid':104749,'childcid':0,'order_rule':0}),)

def market_with_parmas(request,categoryid,childcid,order_rule):
    foodtypes=Foodtype.objects.all()
    if childcid==ALL_TYPE:
        goods_list = Goods.objects.filter(categoryid=categoryid)
    else:
        goods_list=Goods.objects.filter(categoryid=categoryid).filter(childcid=childcid)
    foodtype=Foodtype.objects.get(typeid=categoryid)
#*****************************market排序部分********************************
    #排序规则 ：0代表综合排序 ，1代表价格升序 ，2代表价格降序
    if order_rule ==ORDER_TOTAL:
        pass
    elif order_rule==PRICE_ASC:
        goods_list=goods_list.order_by('price')
    elif order_rule==PRICE_DESC:
        goods_list=goods_list.order_by('-price')



#***************************************************************************
    childtypenames=foodtype.childtypenames
    childtypename_list=childtypenames.split("#")
    child_type_list=[]
    for childtypename in childtypename_list:
        child_type_list.append(childtypename.split(":"))


    data={
        'title':'闪购',
        'foodtypes':foodtypes,
        'goods_list':goods_list,
        'categoryid':int(categoryid),
        'child_type_list':child_type_list,
        'childcid':childcid,
        'order_rule':order_rule


    }
    return render(request,'market/market.html',context=data)
def cart(request):
    data={
        'title':'购物车'
    }
    return render(request,'cart/cart.html',context=data)


def user_register(request):
    if request.method=='GET':
      data={
        'title':'用户注册'
      }
      return render(request,'user/user_register.html',context=data)
    elif request.method=='POST':
       username=request.POST.get('u_name')
       password=request.POST.get('u_password')
       email=request.POST.get("u_email")
       icon=request.FILES.get('u_icon')
       user=UserModel()
       user.u_name=username
       user.u_email=email
       user.u_icon=icon
       user.set_password(password)
       user.save()
       request.session['user_id']=user.id
       send_email_learn(username,email,user.id)
       return redirect(reverse('app:mine'))

#*******************退出登录**********************************
def user_logout(request):
    request.session.flush()
    return redirect(reverse('app:mine'))
#**************用户校验****************************************


def check_user(requset):
    username=requset.GET.get("u_name")
    users= UserModel.objects.filter(u_name=username)#结果是0或1 因为u_name添加了唯一约束
    data={
        'status':'200',
        'msg':'ok'
    }
    if users.exists():
        #801代表用户已经存在
       data['status']='801'
       data['msg']='already exists'
    else:
        data['msg']='canuse'
    return JsonResponse(data)


def check_email(requset):
    email=requset.GET.get('u_email')
    users=UserModel.objects.filter(u_email=email)
    data={
        'status':'200',
        'msg':'ok'
    }
    if users.exists():
       data['status']='802'
       data['msg'] = 'email already exists'
    else:
      data['status']='can use'
    return JsonResponse(data)


def user_login(request):
    if request.method =='GET':
        msg=request.session.get('msg')
        data={
          'title':'用户登录',
          'msg':msg

         }
        return render(request,'user/user_login.html',context=data)
    elif request.method=='POST':
        username =request.POST.get('u_name')
        print (username)
        password=request.POST.get('u_password')
        print (password)
        users=UserModel.objects.filter(u_name=username)
        if users.exists():
            user=users.first()
            if user.check_password(password):
                if not user.is_activate:
                    request.session['msg'] = '用户未激活'
                    return redirect(reverse('app:user_login'))

                request.session['user_id']=user.id
                return redirect('app:mine')
            else:#密码错误
                request.session['msg'] = '密码错误'
                return redirect(reverse('app:user_login'))
        else:#用户不存在
            request.session['msg'] = '用户不存在'
            return redirect(reverse('app:user_login'))

'''
激活
   能找到用户的方式
              -根据用户的唯一标识
   修改用户的状态
'''

def send_email_learn(username,email,userid):
    title='爱先锋VIP激活邮件'
    message=''
    email_from='17694871425@163.com'
    recipent_list=[email,]
    temp=loader.get_template('user/user_activate.html')
    token=str(uuid.uuid4())
    cache.set(token, userid, timeout=60*60)
    data={
        'username':username,
        'activate_url':'http://18.191.148.143:12347/app/activateuser/?utoken=%s'% token
    }
    html=temp.render(data)
    send_mail(title,message,email_from,recipent_list,html_message=html)



def activateuser(request):
    user_token=request.GET.get('utoken')
    user_id=cache.get(user_token)
    if not user_id:
        return  HttpResponse('激活已经过期，请重新申请激活邮件')
    user=UserModel.objects.get(pk=user_id)
    user.is_activate=True
    user.save()
    return HttpResponse('用户激活成功')


def addtocart(request):
    goodsid=request.GET.get('goodsid')
    userid=request.session.get('user_id')
    print (goodsid)

    data={
            'status':'200',
            'msg':'ok'
        }
    if not userid:
        data['status']='302'
        data['msg']='not login'
        return JsonResponse(data)
    else:
        goods=Goods.objects.get(pk=goodsid)
        user=UserModel.objects.get(pk=userid)
        cartmodels=CartModel.objects.filter(c_goods=goods).filter(c_user=user)
        # cartmodels=CartModel.objects.filter(c_goods_id=goodsid).filter(c_user_id=userid)
        if cartmodels.exists():
            cartmodel=cartmodels.first()
            cartmodel.c_goods_nun=cartmodel.c_goods_num+1
            cartmodel.save()
        else:
            cartmodel=CartModel()
            cartmodel.c_goods=goods
            cartmodel.c_user=user
            cartmodel.save()
        data['goods_num']=cartmodel.c_goods_num
    return JsonResponse(data)