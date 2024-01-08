from django.urls import path
from .views import (
		my_fbv,
		CourseView,
		CourseListView,
		MyListView,
		CourseCreateView,
		CourseUpdateView,
		CourseDeleteView,
	)

app_name = 'courses'

urlpatterns = [
	# path('', my_fbv, name='courses-list'),    # 和product非常相似，但是又略有不同
	path('', CourseListView.as_view(), name='courses-list'),
	path('<int:id>/', CourseView.as_view(), name='courses-detail'),
	path('<int:id>/update/',CourseUpdateView.as_view(), name='courses-update'),   # 曾经一个竖线让我debug了好久！
	path('<int:id>/delete/',CourseDeleteView.as_view(), name='courses-delete'), 
	path('create/', CourseCreateView.as_view(), name='courses-create'),

]