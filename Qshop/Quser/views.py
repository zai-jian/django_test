from django.shortcuts import render
from Quser.models import *
import hashlib

#加密
def set_password(password):
    #加密
    md5 = hashlib.md5()
    md5.update(password.encode())
    result = md5.hexdigest()
    return result

#校验用户是否存在
def valid_user(email):
    """
    如果email存在，返回数据
    否则返回false
    :param email:
    :return:
    """
    try:
        user = Quser.objects.get(email=email)
    except Exception as e:
        return False
    else:
        return user
#用户注册函数
def add_user(**kwargs):
    """
    将用户信息存到数据库
    :param kwargs:
    :return:
    """
    if "email" in kwargs and "username" not in kwargs:
        kwargs["username"] = kwargs["email"]
        print(kwargs)
    user = Quser.objects.create(**kwargs)
    return user

def update_user(id,**kwargs):
    pass

def delete_user(id):
    pass



# Create your views here.
