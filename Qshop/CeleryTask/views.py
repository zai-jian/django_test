
from django.shortcuts import render
from django.http import HttpResponse
from CeleryTask.tasks import add
def get_celery(request):

    add.delay()
    return HttpResponse("调用成功")

# Create your views here.
