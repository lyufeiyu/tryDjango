from django.http import HttpResponse    # 其可以处理html代码
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):   # *args, **kwargs
	print(args,kwargs)	# 加了请求后这里的参数都显示为空了
	print(request.user)   # 终端会显示当前登陆该网址的用户
	# return HttpResponse("<h1>Hello World!</h1>")  # string of HTML code
	return render(request,"home.html",{})

def contact_view(request,*args, **kwargs):
	return render(request,"contact.html",{})

def about_view(request,*args, **kwargs):
	my_context={
		"my_text": "This is about us",
		"this_is_true": True,
		"my_number": 123,
		"my_list": [123,4243,312,"abc"],
		"my_html": "<h1>Hello lvfeiyu!</h1>"
	}
	return render(request,"about.html",my_context )

def social_view(*args,**kwargs):
	return HttpResponse("<h1>Social Page</h1>")