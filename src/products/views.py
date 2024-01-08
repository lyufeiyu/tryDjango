from django.http import Http404
from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from .forms import ProductForm,RawProductForm


def product_create_view(request):
	form=ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form=ProductForm()
	context={
		"form": form
	}
	return render(request,"products/product_create.html",context)

def product_update_view(request):
	obj=get_object_or_404(Product,id=id)
	form=ProductForm(request.POST or None,instance=obj)
	if form.is_valid():
		form.save()
	context={
		'form': form
	}
	return render(request,"products/product_create.html",context)

def product_list_view(request):
	queryset = Product.objects.all()    # list of objects  
	context = {
		"object_list": queryset
	}
	return render(request,"products/product_list.html",context)

def product_detail_view(request,my_id):
	obj=get_object_or_404(Product,id=my_id)
	context={
		"object": obj
	}
	return render(request,"products/product_detail.html",context)

def product_delete_view(request,my_id):
	obj=get_object_or_404(Product,id=my_id)
	if request.method=='POST':  # confirming delete
		obj.delete()
		return redirect('../')
	context={
		"object": obj
	}
	return render(request,"products/product_delete.html",context) 


'''
	下面是之前学习练手的

def product_list_view(request):
	queryset = Product.objects.all()    # list of objects  
	context = {
		"object_list": queryset
	}
	return render(request,"products/product_list.html",context)


def product_delete_view(request,my_id):
	obj=get_object_or_404(Product,id=my_id)
	if request.method=='POST':  # confirming delete
		obj.delete()
		return redirect('../')
	context={
		"object": obj
	}
	return render(request,"products/product_delete.html",context) 

# Dynamic URL Routing
def dynamic_lookup_view(request,my_id):  # 参数my_id和urls.py的my_id名字一定要一致
	obj=get_object_or_404(Product,id=my_id)
	obj=Product.objects.get(id=my_id)
	try:
		obj=Product.objects.get(id=my_id)
	except Product.DoesNotExist:
		raise Http404
	context={
		"object":obj
	}
	return render(request,"products/product_detail.html",context)


def render_initial_data(request):
	initial_data = {
		'title': 'my awesome title',
		# 'description': 
	}
	obj=Product.objects.get(id=1)
	# form = RawProductForm(request.POST or None, initial=initial_data, instance=obj)
	form = ProductForm(request.POST or None, instance=obj)
	if form.is_valid(): 
		form.save() # 这里可以通过网页前端更改后端数据
	context = {
		'form': form
	}
	return render(request,"products/product_create.html",context)

# Pure Django Form
# def product_create_view(request):
# 	my_form=RawProductForm()
# 	if request.method == "POST":
# 		my_form=RawProductForm(request.POST)
# 		if my_form.is_valid():
# 			# now the data is good
# 			print(my_form.cleaned_data)
# 			Product.objects.create(**my_form.cleaned_data)
# 		else:
# 			print(my_form.errors)
# 	context={
# 		"form": my_form
# 	}
# 	return render(request,"products/product_create.html",context)

# raw html form
def product_create_view(request):
	form=ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form=ProductForm()
	# print("这是GET----",request.GET)
	# print("这是POST----", request.POST)
	if request.method == 'POST':
		my_new_title=request.POST.get('title')
		print(my_new_title)
	context={
		"form": form
	}
	return render(request,"products/product_create.html",context)

# Create your views here.
def product_detail_view(request):
	obj=Product.objects.get(id=1)
	# context={
	# 	'title': obj.title,
	# 	'description': obj.description,
	# 	# 'description': "aaaaaaaaaaaaa",  # 确实是可以显示的，只不过你之前没有对obj.description赋值
	# 	'price': obj.price,
	# 	'summary': obj.summary,
	# 	'featured': obj.featured
	# }  # 这样的映射很有问题，万一你model那一边
	context={
		"object": obj
	}
	return render(request,"products/product_detail.html",context)

''' 