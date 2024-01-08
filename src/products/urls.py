from django.urls import path
from .views import (
    product_detail_view,
    product_create_view,
    product_delete_view,
    product_list_view,
    product_update_view
)
    
app_name='products'   # 实际上要指定哪个

urlpatterns = [
    path('', product_list_view,name='product-list'),   # 当我这里不用products而是用p时，url会进行更新，从而起到保密的效果
    path('create/', product_create_view,name='product-list'), 
    path('<int:my_id>/', product_detail_view,name='product-detail'),
    path('<int:my_id>/delete/', product_delete_view,name='product-delete'),
    path('<int:my_id>/update/', product_update_view,name='product-update'),
]
