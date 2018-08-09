# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib

from django.db import models
#**************************用户模型*******************************
# class User(models.Model):
#     userAccount=models.CharField(max_length=20,unique=True)#用户账号，要唯一
#     userPasswd=models.CharField(max_length=20)#用户密码
#     username=models.CharField(max_length=20)#用户名称
#     userphone=models.CharField(max_length=11)#手机号
#     userAdderss=models.CharField(max_length=100)#用户地址
#     userImg=models.CharField(max_length=150)#用户头像
#     userRank=models.IntegerField(default=1)#用户等级
#     userToken=models.CharField(max_length=50)#touken验证，每次登录后都会更新
class Home(models.Model):
    img=models.CharField(max_length=300)
    name=models.CharField(max_length=20)
    trackid=models.IntegerField(default=1)

    class Meta:
        abstract=True
class HomeWheel(Home):
    class Meta:
        db_table='axf_wheel'
class HomeNav(Home):
    class Meta:
        db_table='axf_nav'
class HomeMustbuy(Home):
    class Meta:
        db_table='axf_mustbuy'
class HomeShop(Home):
    class Meta:
        db_table='axf_shop'
class HomeMainShow(Home):
    categoryid=models.IntegerField(default=1)
    brandname=models.CharField(max_length=32)
    img1=models.CharField(max_length=200)
    childcid1=models.IntegerField(default=1)
    productid1=models.IntegerField(default=1)
    longname1=models.CharField(max_length=128)
    price1=models.FloatField(default=0)
    marketprice1=models.FloatField(default=0)
    img2=models.CharField(max_length=200)
    childcid2=models.IntegerField(default=1)
    productid2=models.IntegerField(default=1)
    longname2=models.CharField(max_length=128)
    price2=models.FloatField(default=0)
    marketprice2=models.FloatField(default=0)
    img3=models.CharField(max_length=200)
    childcid3=models.IntegerField(default=1)
    productid3=models.IntegerField(default=1)
    longname3=models.CharField(max_length=128)
    price3=models.FloatField(default=0)
    marketprice3=models.FloatField(default=0)
    class Meta:
        db_table='axf_mainshow'
class Foodtype(models.Model):
    typeid=models.IntegerField(default=1)
    typename=models.CharField(max_length=16)
    childtypenames=models.CharField(max_length=200)
    typesort=models.IntegerField(default=1)
    class Meta:
        db_table='axf_foodtypes'
class Goods(models.Model):
    productid=models.IntegerField(default=1)
    productimg=models.CharField(max_length=256)
    productname=models.CharField(max_length=156)
    productlongname=models.CharField(max_length=256)
    isxf=models.BooleanField(default=False)
    pmdesc=models.BooleanField(default=False)
    specifics=models.CharField(max_length=27)
    price=models.FloatField(default=1)
    marketprice=models.FloatField(default=1)
    categoryid=models.IntegerField(default=1)
    childcid=models.IntegerField(default=1)
    childcidname=models.CharField(max_length=128)
    dealerid=models.IntegerField(default=1)
    storenums=models.IntegerField(default=1)
    productnum=models.IntegerField(default=1)
    class Meta:
        db_table='axf_goods'
#************************用户表*****************************
class UserModel(models.Model):
    u_name=models.CharField(max_length=16,unique=True)
    u_password=models.CharField(max_length=128)
    u_email=models.CharField(max_length=256)
    u_icon=models.ImageField(upload_to='icons')
    is_delete=models.BooleanField(default=False)
    is_activate=models.BooleanField(default=False)

    #设置密码
    def __init__(self, *args, **kwargs):
        super(UserModel, self).__init__(*args, **kwargs)
        self.id = None

    def set_password(self,password):

        self.u_password=self.generate_hash(password)
    #对密码进行哈希加密
    def generate_hash(self, password):
        sha = hashlib.sha512()
        sha.update(password.encode('utf-8'))

        return sha.hexdigest()
    #验证密码
    def check_password(self,password):
        return self.u_password==self.generate_hash(password)
    class Meta:
        db_table='axf_usr'

class CartModel(models.Model):
    c_goods_num=models.ImageField(default=1)
    c_goods_select=models.BooleanField(default=True)
    c_goods=models.ForeignKey(Goods)
    c_usr=models.ForeignKey(UserModel)
    class Meta:
        db_table='axf_cart'
