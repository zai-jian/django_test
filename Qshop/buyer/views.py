from django.http import HttpResponseRedirect
from django.shortcuts import render

from Quser.views import valid_user, set_password
from Shop.models import *
def index(request):
    shouye = Goods.objects.all()
    #查询所有类型
    type_list = GoodsType.objects.all()[:3]
    #查询单个类型
    type_data = GoodsType.objects.get(id=1)
    #查询对应类型的所有商品
    type_data.goods_set.all()
    #查询每个类型对应的4个商品
    for t in type_list:
        goods_list = t.goods_set.all()[:4]
    #上述内容进行整理
    result = [{t.name:t.goods_set.all(),"pic":t.picture} for t in type_list]
    message = "fruit"
    return render(request,"buyer/index.html",locals())

def goods_list(request):
    id = request.GET.get("id")
    goods_list = Goods.objects.all()
    if id:
        goods_type = GoodsType.objects.get(id=int(id))
        goods_list = goods_type.goods_set.all()
    return render(request,"buyer/goods_list.html",{"goods_list":goods_list})

def goods(request,id):
    goods_data = Goods.objects.get(id=int(id))
    return render(request,"buyer/goods.html",locals())

def login(request):
    get_referer = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pwd")
        #判断用户是否存在
        # 如果存在
        user = valid_user(email)
        if user:
            #判断密码是否正确
            db_password = user.password
            request_password = set_password(password)
            if db_password == request_password:
                referer = request.POST.get("referer")
                response = HttpResponseRedirect(referer)
                response.set_cookie("email",user.email)
                response.set_cookie("user_id", user.id)
                request.session["email"] = user.email
                return response
            else:
                error = "密码错误"
        else:
            error = "用户不存在"
    return render(request,"buyer/login.html",locals())


# Create your views here.
