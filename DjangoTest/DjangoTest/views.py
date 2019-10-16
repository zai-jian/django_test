from django.shortcuts import render_to_response
from News.models import *

def func(request):
    list1 = New.objects.all()
    return render_to_response('demo.html', locals())