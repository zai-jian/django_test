from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db.models import *
from News.models import *

def func(request):
    list1 = New.objects.all()
    return render_to_response('demo.html', locals())

def add_new_type(request):
    new_type = NewType()
    new_type.label = '背影'
    new_type.decription = '你在此地不要走动'
    new_type.save()
    return HttpResponse("successfully")

def add_new(request):
    new = New()
    new.title = "新闻标题dramatic"
    new.time = "1998-2-2"
    new.description = "新闻描述"
    new.image = "1.jpg"
    new.content = "新闻内容"
    new.type_id = NewType.objects.get(id=1)
    new.save()
    new.editor_id.add(
        Editor.objects.get(id=1)
    )
    new.save()
    return HttpResponse("successful")
def selectExample(request):
    news_list = Editor.objects.get(id=1).new_set.all()
    news_list2 = New.objects.order_by("-id")[:2]
    group_list = New.objects.all().annotate(content = 'content')
    return render_to_response('demo.html', locals())
