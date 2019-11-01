from django.shortcuts import render
from django.http import HttpResponseRedirect
from Quser.views import *
from Shop.models import *
import smtplib
from email.mime.text import MIMEText

def login_valid(fun):
    def inner(request,*args,**kwargs):
        cookie_user = request.COOKIES.get("email")
        session_user = request.session.get("email")
        if cookie_user and session_user and cookie_user == session_user:
            user = Quser.objects.get(email=cookie_user)
            identity = user.identity
            if identity >= 1:
                return fun(request,*args,**kwargs)
            else:
                return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/Shop/login/")

    return inner




def register(request):
    """
    后台卖家注册功能
    :param request:
    :return:
    """
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        #检测用户是否注册过
        #注册过,提示当前邮箱已经注册
        error = " "
        if valid_user(email):
           error = "当前邮箱已经注册"
        #没有注册过
        else:
            #对密码加密
            password = set_password(password)
            #保存到数据库
            add_user(email = email,password = password)
            #跳转到登录
            return HttpResponseRedirect("/Shop/login/")
    return render(request,"shop/register.html",locals())


def login(request):
    """
    后台卖家登录功能
    :param request:
    :return:
    """
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        #判断用户是否存在
        #如果存在
        user = valid_user(email)
        if user:
            #判断密码是否正确
            db_password = user.password
            request_password = set_password(password)
            if db_password == request_password:
                response = HttpResponseRedirect("/Shop/index/")
                response.set_cookie("email",user.email)
                response.set_cookie("user_id",user.id)
                response.set_cookie("picture",user.picture)
                request.session["email"] = user.email
                return response
            else:
                error = "密码错误"
        else:
            error = "用户不存在"
    return render(request,"shop/login.html",locals())

@login_valid
def index(request):
    """
    后台卖家首页
    :param request:
    :return:
    """
    return render(request,"shop/index.html")

def logout(request):
    """
    后台卖家退出登录功能
    :param request:
    :return:
    """
    response = HttpResponseRedirect("/Shop/login/")
    response.delete_cookie("email")
    response.delete_cookie("user_id")
    request.session.clear()
    return response

def reset_password(request):
    """
    重置密码
    接收发过来的邮箱进行校验
    :param request:
    :return:
    """
    if request.method == "POST":
        email = request.POST.get("email")
        if email and valid_user(email):
            #发送邮件的内容
            #首先需要有找回页面的地址
            #其次包含要修改密码的账号
            #再次包含修改时的一个校验码
                #使用当前时间+账号 ==》md5加密
            hash_code = set_password(email)
            content = "http://127.0.0.1:8000/Shop/change_password/?email=%s&token=%s"%(email,hash_code)
            #发送邮件
            sendmail(content,email)
    return HttpResponseRedirect("/Shop/forget_password/")


def change_password(request):
    """
    当前人是否有资格修改密码
    """
    if request.method == "POST":
        email = request.COOKIES.get("change_email")
        password = request.POST.get("password")

        e = Quser.objects.get(email=email)
        e.password = set_password(password)
        e.save()
        return HttpResponseRedirect("/Shop/login/")

    email = request.GET.get("email")
    token = request.GET.get("token")

    now_token = set_password(email)
    #当前提交人存在并且token值正确
    if  valid_user(email) and now_token == token:
        response = render(request,"shop/change_password.html")
        response.set_cookie("change_email",email)
        return response

    else:
        return HttpResponseRedirect("/Shop/forget_password/")

def forget_password(request):
    """
    后台卖家忘记密码功能
    :param request:
    :return:
    """
    return render(request,"shop/forgot-password.html")
# Create your views here.

from Quser.models import Quser
@login_valid
def profile(request):
    """
    个人中心
    :param request:
    :return:
    """
    user_email = request.COOKIES.get("email")
    user = Quser.objects.get(email=user_email)
    if request.method == "POST":
        password = request.POST.get("password")
        user.password = set_password(password)
        user.save()

        response = HttpResponseRedirect("/Shop/login/")
        response.delete_cookie("email")
        response.delete_cookie("user_id")
        request.session.clear()
        return response
    return render(request,"shop/profile.html",{"user":user})
@login_valid
def set_profile(request):
    user_email = request.COOKIES.get("email")
    user = Quser.objects.get(email=user_email)
    if request.method == "POST":
        post_data = request.POST
        username = post_data.get("username")
        gender = post_data.get("gender")
        age = post_data.get("age")
        phone = post_data.get("phone")
        address = post_data.get("address")
        picture = request.FILES.get("picture")

        user.username = username
        user.gender = gender
        user.age = age
        user.phone = phone
        user.address = address
        if picture:
            user.picture = picture
        user.save()
        return HttpResponseRedirect("/Shop/profile/")
    return render(request,"shop/set_profile.html",{"user":user})
@login_valid
def add_goods(request):
    if request.method == "POST":
        post_data = request.POST
        name = post_data.get("name")
        price = post_data.get("price")
        number = post_data.get("number")
        production = post_data.get("production")
        safe_date = post_data.get("safe_date")
        description = post_data.get("description")
        picture = request.FILES.get("picture")
        goods_type_id = post_data.get("goods_type")


        goods = Goods()
        goods.statue = 1
        goods.name = name
        goods.price = price
        goods.number = number
        goods.production = production
        goods.safe_date = safe_date
        goods.description = description
        goods.picture = picture
        goods.goods_type_id = goods_type_id
        goods.save()
        return HttpResponseRedirect("/Shop/list_goods/")

    return render(request,"shop/add_goods.html")

def list_goods(request):
    email = request.COOKIES.get("email")
    user = Quser.objects.get(email=email)
    goods_list = user.goods_set.all()
    return render(request,"shop/list_goods.html",locals())

def set_goods(request,id):
    """

    :param id: 锁定商品的标识
    :param set_type: up上架  down下架
    :return:
    """
    set_type = request.GET.get("set_type")
    goods = Goods.objects.get(id=int(id))
    if set_type == "up":
        goods.statue = 1
    elif set_type == "down":
        goods.statue = 0
    goods.save()
    return HttpResponseRedirect("/Shop/list_goods/")

def goods(request,id):
    goods_data = Goods.objects.get(id=int(id))
    return render(request,"shop/goods.html",locals())

def update_goods(request,id):
    goods_data = Goods.objects.get(id=int(id))
    if request.method == "POST":
        post_data = request.POST
        name = post_data.get("name")
        price = post_data.get("price")
        number = post_data.get("number")
        production = post_data.get("production")
        safe_date = post_data.get("safe_date")
        description = post_data.get("description")
        picture = request.FILES.get("picture")
        goods_type_id = post_data.get("goods_type")

        print(goods_type_id)

        goods_data.statue = 1
        goods_data.name = name
        goods_data.price = price
        goods_data.number = number
        goods_data.production = production.replace("年","-").replace("月","-").replace("日","")
        goods_data.safe_date = safe_date
        goods_data.description = description
        goods_data.goods_type_id = goods_type_id
        if picture:
            goods_data.picture = picture
        goods_data.save()
        return HttpResponseRedirect("/Shop/goods/%s/"%id)

    return render(request,"shop/update_goods.html",locals())

def merge_goods(request,id=0):
    if id:
        goods_data = Goods.objects.get(id=int(id))
    else:
        goods_data = Goods()
    if request.method == "POST":
        post_data = request.POST
        name = post_data.get("name")
        price = post_data.get("price")
        number = post_data.get("number")
        production = post_data.get("production")
        safe_date = post_data.get("safe_date")
        description = post_data.get("description")
        goods_type_id = post_data.get("goods_type_id")
        picture = request.FILES.get("picture")



        goods_data.statue = 1
        goods_data.name = name
        goods_data.price = price
        goods_data.number = number
        goods_data.production = production.replace("年","-").replace("月","-").replace("日","")
        goods_data.safe_date = safe_date
        goods_data.description = description
        goods_data.goods_type_id = goods_type_id
        if picture:
            goods_data.picture = picture
        goods_data.save()
        return HttpResponseRedirect("/Shop/goods/%s/"%goods_data.id)

    return render(request,"shop/merge.html",locals())



from django.views import View
from django.http import JsonResponse
from django.core.paginator import Paginator
from Qshop.settings import PAGE_SIZE
class GoodsView(View):
    def get(self,request):
        result = {
            "version":"v1",
            "code":"200",
            "data":[],
            "page_range":[],
            "referer":""
        }
        id = request.GET.get("id")#尝试获取前端get提交的id
        #如果id存在获取当前id的数据
        if id:
            goods_data = Goods.objects.get(id=int(id))
            result["data"].append(
                {
                  "id":goods_data.id,
                  "name":goods_data.name,
                  "number":goods_data.number,
                  "production":goods_data.production,
                  "safe_date":goods_data.safe_date,
                  "picture":goods_data.description,
                  "statue":goods_data.statue
                }
            )
        #如果id不存在获取所有数据
        else:
            # 尝试获取页码，如果页码不存在，默认是第一页
            page_number = request.GET.get("page",1)
            #尝试获取查询的值
            keywords = request.GET.get("keywords")
            #获取所有数据
            all_goods = Goods.objects.all()
            if keywords:#如果有值，查询对应值
                all_goods = Goods.objects.filter(name__contains=keywords)
                result["referer"] = "&keywords=%s"%keywords
            #进行分页
            paginator = Paginator(all_goods,PAGE_SIZE)
            #获取单页数据
            page_data = paginator.page(page_number)
            #获取页码
            result["page_range"] = list(paginator.page_range)
            #对当前页面数据进行遍历，形成字典，进行Jason封装
            goods_data = [{
                    "id":g.id,
                    "name":g.name,
                    "price": g.price,
                    "number": g.number,
                    "production": g.production,
                    "safe_date": g.safe_date,
                    "picture": g.picture.url,
                    "description": g.description,
                    "statue": g.statue} for g in page_data
            ]
            result["data"] = goods_data
        return JsonResponse(result)
@login_valid
def vue_list_goods(request):
    return render(request,"shop/vue_list_goods.html")

@login_valid
def change_goods(request,id=0):
    type_list = GoodsType.objects.all()
    if id:
        goods_data = Goods.objects.get(id=id)
    else:
        goods_data = Goods()
    if request.method == "POST":
        post_data = request.POST
        name = post_data.get("name")
        price = post_data.get("price")
        number = post_data.get("number")
        production = post_data.get("production")
        safe_date = post_data.get("safe_date")
        description = post_data.get("description")
        goods_type = post_data.get("goods_type")
        picture = request.FILES.get("picture")

        goods_data.name = name
        goods_data.price = price
        goods_data.number = number
        goods_data.production = production.replace("年", "-").replace("月", "-").replace("日", "")
        goods_data.safe_date = safe_date
        goods_data.description = description
        #保存商品类型
        goods_data.goods_type = GoodsType.objects.get(id=int(goods_type))
        #保存商店
        #获取cookie当中的店铺
        store_id = request.COOKIES.get("email")
        #获取店铺信息
        goods_data.goods_store = Quser.objects.get(email=store_id)

        if picture:
            goods_data.picture = picture
        goods_data.save()
        return HttpResponseRedirect("/Shop/goods/%s/"%goods_data.id)
    return render(request,"shop/change_goods.html",locals())

# from email.header import Header
# def sendmail(content,email):
#     from Qshop.settings import MAIL_PORT,MAIL_SENDER,MAIL_SERVER,MAIL_PASSWORD
#
#     content = """
#     请确认是本人修改密码，点击下方链接修改密码
#     <a href="%s">点击链接确认</a>
#     """%content
#
#     print(content)
#
# #构建邮件格式
#     message = MIMEText(content,"html","utf-8")
#     message["To"] = Header(email,'utf-8')
#     message["From"] = Header(MAIL_SENDER,'utf-8')
#     message["Subject"] = Header('你猜我是谁','utf-8')
#
# #发送邮件
#     smtp = smtplib.SMTP()
#     smtp.connect(MAIL_SERVER,25)
#     smtp.login(MAIL_SENDER,MAIL_PASSWORD)
#     smtp.sendmail(MAIL_SENDER,email,message.as_string())
#     print('发送成功')
#
# from django.http import HttpResponse
# from CeleryTask.tasks import add
# from CeleryTask.tasks import sendmail as SDM
# def get_celery(request):
#
#     add.delay()
#     SDM.delay()
#     #print(add.result)
#     return HttpResponse("调用完成")
#
# from Shop.models import GoodsType
# def example(request):
#     all_data = GoodsType.objects.all()
#     four_goods = GoodsType.objects.hello(1)
#     return render(request,"shop/Example.html",locals())