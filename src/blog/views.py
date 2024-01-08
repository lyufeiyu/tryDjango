from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse

from django.views.generic import (
		CreateView,
		DetailView,
		ListView,
		UpdateView,
		DeleteView
	)

from .models import Article
from .forms import ArticleModelForm

# Create your views here. 

class ArticleCreateView(CreateView):
	template_name = 'articles/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all()     # <blog>/<modelname>_list.html
	# success_url = '/'		# 我创建成功后是想看看内容的，还是不要覆盖了

	def form_valid(self,form):
		print(form.cleaned_data)
		return super().form_valid(form)

	# def get_success_url(self):		# 这是另外一种成功后覆盖url的方法，但是默认方法同样生效的
	# 	return '/'


class ArticleListView(ListView):
	template_name = 'articles/article_list.html'
	queryset = Article.objects.all()     # <blog>/<modelname>_list.html

class ArticleDetailView(DetailView):	# 这种与product不同的方法可能让人confusing，但是非常简便啊，这里的all查询是没用滴
	template_name = 'articles/article_detail.html'
	queryset = Article.objects.all()    # 
	# queryset = Article.objects.filter(id__gt=1) 

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article,id=id_)

class ArticleUpdateView(UpdateView):
	template_name = 'articles/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all() 
	
	def get_object(self):	# 抓取一个对象或者是一个对象的实例
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article,id=id_)

	def form_valid(self,form):  # 会自动执行该函数的，实际上这些代码都会被执行以更新，虽说比较难理解，但是后面相信我自然就会懂
		print(form.cleaned_data)
		return super().form_valid(form)

class ArticleDeleteView(DeleteView):	# 这种与product不同的方法可能让人confusing，但是非常简便啊，这里的all查询是没用滴
	template_name = 'articles/article_delete.html'
	success_url = '/blog/'		# 再说一遍，这个写了就会自动执行，删除成功后，会跳转到该url，但这里我们也可以用下面的函数

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article,id=id_)

	def get_success_url(self):		# 作用和success_url='/blog/'一样
		return reverse('articles:article-list')

'''
	Function Based View to Class Based View
	上面是class based view
	下面是function based view
	我们能很明显看出上下两种的差别，下面的基于函数的视图明显好理解一些
'''

def article_detail_view(request,my_id):
	obj=get_object_or_404(Article,id=my_id)
	context={
		"object": obj
	}
	return render(request,"articles/article_detail.html",context)




