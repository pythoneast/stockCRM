from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('view/<int:pk>', views.user_view, name='user_view'),
    path('create', views.user_create, name='user_create'),
    path('update/<int:pk>', views.user_update, name='user_update'),
]
