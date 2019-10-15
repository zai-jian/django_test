"""DjangoFirst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from DjangoFirst.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',index),
    re_path('say/(?P<mouth>.+)/(?P<day>.+)/',say),
    path('my_test/',my_test),
    path('test/',test),
    path('index_page/', index_page),
    path('func2/', func2),
    path('list_page/', list_page),
    path('shop/', shop),
    path('shop_list1/', shop_list1),
    path('shop_list2/', shop_list2),
    path('shop_list3/', shop_list3),
    path('shop_list4/', shop_list4),
    path('shop_list5/', shop_list5),
    path('shop_list6/', shop_list6),
    path('shop_list7/', shop_list7),
    path('shop_list8/', shop_list8),
    path('shop_list9/', shop_list9),

]
