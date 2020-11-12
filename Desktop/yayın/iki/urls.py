"""iki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('isyeriekle/' , include('isyeriekle.urls')) ,
    url('firmalar/' , include('calisilanFirma.urls')) ,
    url('evrakAdi/' , include('evrakAdi.urls')) ,
    url('eslestirme/' , include('eslestirme.urls')) ,
    url('dosyayukle/' , include('dosyayukle.urls')) ,
    url('dosyaonay/' , include('dosyaonay.urls')) ,
    url('dokumanlar/' , include('dokumanlar.urls')) ,
    url('' , include('login.urls')) ,

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
