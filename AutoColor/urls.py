"""AutoColor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
# from ImageModel.views import uploadImg,showImg,style_image_show
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import Image_process


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('home/', views.home),
    path('result/', views.result),
    # path('home/', uploadImg),
    # path('home/', showImg),
    path('testimg/',Image_process.Image_process),
    path('test/',Image_process.uploadImg),
    path('test2/',Image_process.showImg),
    path('test3/',Image_process.uploadStyleImg),
    # path('home/', style_image_show)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


