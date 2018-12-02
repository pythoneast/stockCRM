from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('view/<int:pk>', views.product_view, name='product_view'),
    path('create', views.product_create, name='product_create'),
    path('update/<int:pk>', views.product_update, name='product_update'),
    path('delete', views.product_delete, name='product_delete'),
    path('sell', views.sell_product, name='product_sell'),
]
