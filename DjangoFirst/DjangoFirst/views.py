from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world")

def say_hello(request):
    return HttpResponse("<h1 color='red'>hello world</h1>")

def my_test(request):
    return HttpResponse("<span style=color:red>再渐</span>")