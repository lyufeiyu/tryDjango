from django.shortcuts import render,get_object_or_404,redirect
from django.views import View   # 我们想继承基本视图类 
from .models import Course
from .forms import CourseModelForm
# Create your views here.

# BASE VIEW CLASS = View

class CourseObjectMixin(object):  # 是用来减少代码工作量的，减少冗余
	model = Course
	# lookup = 'id'

	def get_object(self): 
		# id = self.kwargs.get(self.lookup)
		id = self.kwargs.get("id ")
		obj=None
		if id is not None:
			obj=get_object_or_404(self.model,id=id)
		return obj

# 专注上面的对象，可以减少代码冗余，所有函数都可以这么操作
class CourseDeleteView(CourseObjectMixin,View): 
	template_name = 'courses/course_delete.html'  

	# def get_object(self):
	# 	id = self.kwargs.get('id')
	# 	obj=None
	# 	if id is not None:
	# 		obj=get_object_or_404(Course,id=id)
	# 	return obj 

	def get(self,request,id=None,*args,**kwargs):
		# GET method
		context={}
		obj=self.get_object()
		if obj is not None:
			context['object']=obj 
		return render(request,self.template_name,context)

	def post(self,request,id=None,*args,**kwargs):  
		# POST method
		context={}
		obj=self.get_object()
		if obj is not None:
			obj.delete()
			context['object']=None
			return redirect('/courses/')
		return render(request,self.template_name,context)

class CourseUpdateView(View): 
	template_name = 'courses/course_update.html'  

	def get_object(self):
		id = self.kwargs.get('id')
		obj=None
		if id is not None:
			obj=get_object_or_404(Course,id=id)
			# context['object']=obj
		return obj 

	def get(self,request,id=None,*args,**kwargs):
		# GET method
		context={}
		obj=self.get_object()
		if obj is not None:
			form =  CourseModelForm(instance=obj)
			context['object']=obj
			context['form']=form
		return render(request,self.template_name,context)

	def post(self,request,id=None,*args,**kwargs):  
		# POST method
		context={}
		obj=self.get_object()
		if obj is not None:
			form = CourseModelForm(request.POST,instance=obj)
			if form.is_valid():
				form.save()
			context['object']=obj
			context['form']=form
		return render(request,self.template_name,context)

class CourseCreateView(View): 
	template_name = 'courses/course_create.html' 
	def get(self,request,*args,**kwargs):  
		# GET method
		form =  CourseModelForm()
		context={'form':form}
		return render(request,self.template_name,context)
	def post(self,request,*args,**kwargs):  
		# POST method
		form =  CourseModelForm(request.POST)
		# 重点来了，创建好之后，你要保存啊！！！
		if form.is_valid():
			form.save()
			# 我要想在点击save按钮之后恢复原状，只需要下面一句代码
			form =  CourseModelForm()
		context={'form':form}
		return render(request,self.template_name,context)

class CourseListView(View):
	template_name = 'courses/course_list.html' 
	queryset = Course.objects.all()

	def get_queryset(self):  # queryset=Course.objects.all()不能删
		return self.queryset

	def get(self,request,*args,**kwargs):
		context = {'object_list': self.get_queryset()}
		return render(request,self.template_name,context)

class MyListView(CourseListView):	# 继承视图CourseListView，筛选出我想要的视图
	queryset = Course.objects.filter(id=1)

class CourseView(View): #DetailView
	'''
	def get(self,request,*args,**kwargs):  这个函数和下面用template_name=about.html的作用是一样的
		# GET method
		return render(request,'about.html',{})
	'''
	# template_name = 'about.html'
	template_name = 'courses/course_detail.html'  #DetailView
	def get(self,request,id=None,*args,**kwargs):  # 基于类的视图函数名称是很重要的，不能随便起
		# GET method
		context={}
		if id is not None:
			obj=get_object_or_404(Course,id=id)
			context['object']=obj
		return render(request,self.template_name,context)

	# def post(request,*args,**kwargs):  # 基于类的视图函数名称是很重要的，不能随便起
	# 	return render(request,'about.html',{})
 

# HTTP METHOD
def my_fbv(request,*args,**kwargs):  #这是一个相当标准的基于函数的视图，它真正所做的只是渲染出来，
	print(request.method)
	return render(request,'about.html',{})

