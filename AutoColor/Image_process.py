from django.http import HttpResponse
from django.shortcuts import render
from ImageModel.models import Img
from ImageModel.models import StyleImg


# 数据库操作
def Image_process(request):
    # img = file.read
    # test1 = Img(name='style1',img='./AttentionedDeepPaint/data/test/test1.png',img_type=1)
    # test1.save()
    return HttpResponse("<p>数据添加成功！</p>")

def uploadImg(request):
    if request.method == 'POST':
        new_img = Img(
        img=request.FILES.get('img'),
        name = request.FILES.get('img').name,
        img_type = 1
        )
        new_img.save()
    return render(request, 'test.html')

def uploadStyleImg(request):
    if request.method == 'POST':
        new_img = StyleImg(
        img=request.FILES.get('img'),
        name = request.FILES.get('img').name,
        img_type = 2
        )
        new_img.save()
    return render(request, 'test3.html')


def showImg(request):
    imgs = Img.objects.all()
    content = {
        'imgs':imgs,
        }
    for i in imgs:
        print (i.img.url)
    return render(request, 'test2.html', content)

def getnamelist (image):
    image = list(image.values())
    new_image = []
    for i in image :
        j = i['name'][:-4]
        new_image.append(j)
    return new_image