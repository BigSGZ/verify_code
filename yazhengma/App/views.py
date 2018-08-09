# -*- coding: utf-8 # encoding: utf-8
from __future__ import unicode_literals

import random
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def get_verify_code(request):
    mode='RGB'
    image_size=(400,300)
    image_color=get_color()
    # 创造画布
    image=Image.new(mode,image_size,image_color)
    # 创造画笔
    image_draw=ImageDraw.Draw(image,mode)
    font_path='static/fonts/ADOBEARABIC-BOLD.OTF'

    image_font = ImageFont.truetype(font_path,size=200)
    source_str='12343567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    dest_str=''
    for i in range(4):
        r=random.randrange(len(source_str))
        dest_str +=source_str[r]
    print (dest_str)
    request.session['verifycode']=dest_str
    for i in range(4):
        image_draw.text((10+100*i,20),dest_str[i],font=image_font,fill=get_color())
    # image_draw.text((20,20),'R',font=font)
    # image_draw.text((60,20),'o',font=font)
    # image_draw.text((100,20),'c',font=font)
    # image_draw.text((140,20),'k',font=font)
    # IO流
    # 内存中引入了输入输出流
    for i in range(3000):
        image_draw.point((random.randrange(image_size[0]),random.randrange(image_size[1])),fill=get_color())
    buffer=BytesIO()
    image.save(buffer,'png')
    return HttpResponse(buffer.getvalue(),content_type='image/png')
def get_color():
    red=random.randrange(256)
    green=random.randrange(256)
    blue=random.randrange(256)
    return (red ,green,blue)


def user_login(request):
    if request.method=='GET':
        return render(request,'userlogin.html')
    elif request.method=='POST':
        verify_code=request.POST.get('verifycode')
        dest_code=request.session.get('verifycode')
        print (verify_code)
        print (dest_code)
        if dest_code.lower()==verify_code.lower():
        # if (dest_code.lower() == verify_code.lower())| (dest_code.upper()==verify_code.upper()):
            return  HttpResponse('验证成功，正在获取个人信息')

        return HttpResponse('验证码错误')
