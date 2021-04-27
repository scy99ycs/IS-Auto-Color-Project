import os
import torch
from PIL import Image
from AttentionedDeepPaint.colorize import colorize_img
from ImageModel.models import StyleImg
from AttentionedDeepPaint.preprocess import save_image
from . import Image_process

from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib import auth
import json

def login(request):
    context ={}
    context['hello'] = 'Hello World!'
    return  render (request, 'login.html',context)

def home(request):

    style_img = []
    style = StyleImg.objects.all()
    for i in range(1,len(style)):
        style_img_ele = StyleImg.objects.get(id=i).__dict__
        style_img.append(style_img_ele)
    style_img_list_name = style.values('name')
    style_img_list_img = style.values('img')
    style_img_list_name_show = Image_process.getnamelist(style_img_list_name)
    style_img_list_img_show = '/media/' + list(style_img_list_img)[0]['img']


    return render(request,'home.html', {
        "style_img" : style_img,
        "style_img_list_name_show" : style_img_list_name_show,
        "style_img_list_img_show" : style_img_list_img_show
    }
                  )

def result(request):
    context = {}
    return render(request,'Result.html',context)





