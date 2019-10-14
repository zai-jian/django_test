from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world")

def say_hello(request, name):
    strings = "<h1 color='red'>hello world %s</h1>"%name
    return HttpResponse(strings)

def my_test(request):
    return HttpResponse("<span style=color:red>再渐</span>")
