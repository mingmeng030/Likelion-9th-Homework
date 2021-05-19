"""firstproject URL Configuration

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
from firstapp import views as first
from wordCount import views as wc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', first.welcome, name="welcome"), #url주소가 안적혀있는데 서버를 기동시키고 처음에 들어가는 페이지가 welcome페이지가 되기 위함
    path('hello/', first.hello, name="hello"),
    path('wc/', wc.home, name="wc"),
    path('wc/result/', wc.result, name="result"),
]
