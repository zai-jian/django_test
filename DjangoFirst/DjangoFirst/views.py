from django.http import HttpResponse
import time

def index(request):
    return HttpResponse("hello world")

def say(request, mouth, day):
    time1 = time.localtime(time.mktime((2019, int(mouth), int(day), 0, 0, 0, 0, 0, 0))).tm_yday
    strings = "<h1 color='red'>生日:{}月{}日 在本年第{}天</h1>".format(mouth, day, time1)
    return HttpResponse(strings)

def my_test(request):
    return HttpResponse("<span style=color:red>再渐</span>")

def test(request):
    string = """
   <!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	<script type="text/javascript">
		var str = '<table border="1">'
		for(var i=1;i<=9;i++){
			if (i%2==0) {
				str+='<tr style="background:red">';
			}else{
				str+='<tr style="background:green">';
			}
			
			for(var j=1;j<=i;j++){
				str += '<td>'+j+"*"+i+"="+i*j+'</td>';

			}
				str+='</tr>'
		}
			str+='</table>'
			document.write(str)


	</script>
</body>
</html>
    
    """
    return HttpResponse(string)