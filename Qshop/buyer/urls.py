from django.urls import path,re_path
from buyer.views import goods_list, index, goods, login

urlpatterns = [
    re_path(r"^$",index),
    path('index/',index),
    re_path(r'goods/(?P<id>\d+)/',goods),
    path('goods_list/',goods_list),
    path('login/',login)

]