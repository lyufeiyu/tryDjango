"""
URL configuration for trydjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from pages.views import home_view, contact_view, about_view
    

urlpatterns = [
    path('products/', include('products.urls')),
    path('blog/', include('blog.urls')),
    path('courses/', include('courses.urls')),
    
    path('', home_view, name='home'),
    path('about/<int:my_id>/', about_view,name='product-detail'),
    path('contact/', contact_view),
    # path('create/', product_create_view),
    # path('initial/', render_initial_data),
    path('admin/', admin.site.urls),

    # path('products/', product_list_view,name='product-list'),   # 当我这里不用products而是用p时，url会进行更新，从而起到保密的效果
    # path('products/create/', product_create_view,name='product-list'), 
    # path('products/<int:my_id>/', product_detail_view,name='product-detail'),
    # path('products/<int:my_id>/delete/', product_delete_view,name='product-delete'),
    # path('products/<int:my_id>/update/', product_update_view,name='product-update'),
]
