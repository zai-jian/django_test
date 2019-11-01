from django.db import models

class Quser(models.Model):
    email = models.EmailField(blank=True,null=True)
    password = models.CharField(max_length=32,blank=True,null=True)

    username = models.CharField(max_length=32,blank=True,null=True,default=email)
    gender = models.CharField(max_length=8,blank=True,null=True)
    age = models.IntegerField(blank=True,null=True)
    phone = models.CharField(max_length=32,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    picture = models.ImageField(upload_to="image",default="/image/0.jpg")

    identity = models.IntegerField(default=0)  # 买家 0 卖家1 平台2
# Create your models here.
