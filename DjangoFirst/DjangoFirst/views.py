from django.http import HttpResponse
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
    return HttpResponse(string)


