from django.http import HttpResponse

def index(request):
    return HttpResponse("hello world")

def say_hello(request):
    return HttpResponse("<h1 color='red'>hello world</h1>")