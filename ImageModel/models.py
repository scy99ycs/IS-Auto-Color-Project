from __future__ import unicode_literals
from django.db import models


class Img(models.Model):
    name = models.CharField(max_length=20,default='test')
    img = models.ImageField(upload_to='img')
    img_type = models.IntegerField(default=0)

class StyleImg(models.Model):
    name = models.CharField(max_length=20,default='test')
    img = models.ImageField(upload_to='style_img')
    img_type = models.IntegerField(default=0)