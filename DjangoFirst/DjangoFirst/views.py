from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
import time
import random

list1 = ['red','blue','green','orange','yellow','pink','purple']

def func():
    for i in range(1,10):
        for j in  range(1,i+1):
            print(i*j,end="  ")
        print()

def index(request):
    return HttpResponse("hello world")

def say(request, mouth, day):
    time1 = time.localtime(time.mktime((2019, int(mouth), int(day), 0, 0, 0, 0, 0, 0))).tm_yday
    strings = "<h1 color='red' align='center'>生日:{}月{}日 在本年第{}天</h1>".format(mouth, day, time1)
    return HttpResponse(strings)

def my_test(request):
    return HttpResponse("<span style=color:red>再渐</span>")

def test(request):
    string = "<table border=1>"
    for i in range(1, 10):
        string += '<tr >'
        for j in range(1, i + 1):
            string += '<td style =background:'+random.choice(list1) +'> ' + str(j) + '*' + str(i) +'='+ str(i * j) + '</td>'
        string += '</tr>'
    string += '</table>'
    string += "<table border=1>"
    for i in range(1, 10):
        string += '<tr >'
        for j in range(1, i + 1):
            string += '<td style =background:'+random.choice(list1) +'> ' + str(j) + '*' + str(i) +'='+ str(i * j) + '</td>'
        string += '</tr>'
    string += '</table>'
    return HttpResponse(string)
def index_page(request):
    template = get_template("index.html")
    response = template.render(
        {
            "name":'didi'
        }
    )
    return HttpResponse(response)

def func2(request):
    test_list = [
        {"商品主页": "农夫山泉",  "我的订单": "无", "我的信息":"老王"},
        {"商品主页": "百岁山", "我的订单": "无", "我的信息": "老刘"},
        {"商品主页": "哇哈哈", "我的订单": "无", "我的信息": "老赵"},
        {"商品主页": "旺仔", "我的订单": "无",  "我的信息": "老钱"},
        {"商品主页": "纯净水", "我的订单": "无", "我的信息": "老孙"}
    ]
    return render_to_response("index.html",locals())

def list_page(request):
    legend_list = [
        {"name":"瑞文",  "sex": "女", "nickname": "放逐之刃", 'url':"/static/images/rv.jpg"},
        {"name": "艾克", "sex": "男", "nickname": "时间刺客", 'url': "/static/images/aik.jpg "},
        {"name": "提莫", "sex": "男", "nickname": "迅捷斥候", 'url': " /static/images/tm.jpg"},
        {"name": "李青", "sex": "男", "nickname": "盲僧", 'url': " /static/images/lq.jpg"},
        {"name": "亚索", "sex": "男", "nickname": "疾风剑豪", 'url': "/static/images/ys.jpg "}
    ]
    return render_to_response("list01.html", locals())

def shop(request):
    city_list = [
        {"name":"朝阳区", "src":"/static/img/shop-pic1.jpg", "style":0, "class": 0},
        {"name": "朝阳区", "src": "/static/img/shop-pic2.jpg", "style": 0,"class": 0},
        {"name": "朝阳区", "src": "/static/img/shop-pic3.jpg", "style": 1,"class": 0},
        {"name": "朝阳区", "src": "/static/img/shop-pic4.jpg", "style": 0,"class": 0},
        {"name": "朝阳区", "src": "/static/img/shop-pic5.jpg", "style": 0,"class": 0},
        {"name": "朝阳区", "src": "/static/img/shop-pic6.jpg", "style": 1,"class": 0},

    ]
    return  render_to_response('shop.html', locals())
def shop_list1(request):
    return render_to_response("about-us.html", locals())
def shop_list2(request):
    return render_to_response("index.html",locals())
def shop_list3(request):
    return render_to_response("meishi-con.html",locals())
def shop_list4(request):
    return render_to_response("meishi.html",locals())
def shop_list5(request):
    return render_to_response("news.html",locals())
def shop_list6(request):
    return render_to_response("news-con.html",locals())
def shop_list7(request):
    return render_to_response("pinpai.html",locals())
def shop_list8(request):
    return render_to_response("shop.html",locals())
def shop_list9(request):
    return render_to_response("shop-con.html",locals())