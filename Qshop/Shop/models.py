from django.db import models
from ckeditor.fields import RichTextField

from Quser.models import Quser


class GoodsTypeManager(models.Manager):
    def hello(self,id):
        return self.get(id=id).goods_set.all()[:4]

class GoodsType(models.Model):
    name = models.CharField(max_length=32)
    picture = models.ImageField(upload_to="shop/img",default="shop/img/1.jpg")
    objects = GoodsTypeManager()


class Goods(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
    number = models.IntegerField()
    production = models.DateTimeField()
    safe_date = models.CharField(max_length=21)
    picture = models.ImageField(upload_to="shop/img",default="shop/img/0.jpg")
    description = RichTextField()
    statue = models.IntegerField()

    goods_type = models.ForeignKey(to=GoodsType, on_delete=models.CASCADE, default=1)
    goods_store = models.ForeignKey(to=Quser, on_delete=models.CASCADE)
# Create your models here.
