from django.shortcuts import render
from ImageModel.models import Img
from ImageModel.Image_froms import image
from ImageModel import models
from django.http import HttpResponse
# Create your views here.

def style_image_show(request):
    if request.method == "GET":
        form = image()
        return render(request, "home.html", {"form": form})
    else:
        form = image(request.POST)
        if form.is_valid():  #
            #
            data = form.cleaned_data  #
            data.pop('r_salary')
            print(data)

            models.StyleImg.objects.create(**data)
            imgs = Img.objects.all()
            for i in imgs:
                print(i.img.url)
            return HttpResponse(
                'ok'
            )
            # return render(request, "add_emp.html", {"form": form})
        else:
            print(form.errors)    #
            clean_errors = form.errors.get("__all__")
            print(222, clean_errors)
        return render(request, "home.html", {"form": form, "clean_errors": clean_errors})

def uploadImg(request): #
    if request.method == 'POST':
        img = Img(img_url=request.FILES.get('img'))
        img.save()
    return render(request, 'home.html')

def showImg(request):
    new_img = Img(img=request.FILES.get('img'))
    new_img.save()
    content = {
        'sketch_img': new_img,
    }
    return render(request, 'home.html', content)

