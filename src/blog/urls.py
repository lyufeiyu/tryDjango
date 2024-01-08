from django.urls import path
from .views import (
		ArticleDetailView,
		ArticleListView,
		ArticleCreateView,
		ArticleUpdateView,
		ArticleDeleteView,
		article_detail_view,

	)

app_name = 'articles'

urlpatterns = [
	path('', ArticleListView.as_view(), name='article-list'),    # 和product非常相似，但是又略有不同
	path('create/', ArticleCreateView.as_view(), name='article-create'), 
	path('<int:id>/', ArticleDetailView.as_view(),name='article-detail'),   # '<int:pk>/',根据报错提示只能用pk或者slug，不能用id,要想用id可以在class里面加一个函数
	path('<int:id>/update/', ArticleUpdateView.as_view(),name='article-update'),
	path('<int:id>/delete/', ArticleDeleteView.as_view(),name='article-delete'), 
]