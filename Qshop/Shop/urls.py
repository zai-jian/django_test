from django.urls import path,re_path
from Shop.views import *

urlpatterns = [
    re_path(r'^$',index),
    path("index/",index),
    path("register/",register),
    path("login/",login),
    path("logout/",logout),
    path("forget_password/",forget_password),
    path("reset_password/",reset_password),
    path("change_password/",change_password),
    path("profile/",profile),
    path("set_profile/",set_profile),
    path("add_goods/",add_goods),
    path("list_goods/",list_goods),
    re_path(r"^set_goods/(?P<id>\d+)",set_goods),
    re_path(r"^goods/(?P<id>\d+)",goods),
    re_path(r"^update_goods/(?P<id>\d+)",update_goods),
    path("Goods/",GoodsView.as_view()),
    path("vue_list_goods/",vue_list_goods),
    path("merge_goods/",merge_goods),
    re_path(r"^merge_goods/(?P<id>\d+)",merge_goods),

    path("change_goods/",change_goods),
]
# urlpatterns +=[
#     path("get_celery/",get_celery),
#     path('example/',example)
#
# ]