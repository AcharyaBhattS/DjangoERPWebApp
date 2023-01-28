# -*- coding: utf-8 -*-
# from django.urls import path
# from . import views

from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home),
    path('contact',views.Contact),
    path('db', views.ProductList.as_view(), name='product_list'),
    path('view/<int:pk>', views.ProductDetail.as_view(), name='product_view'),
    path('new', views.ProductCreate.as_view(), name='product_new'),
    path('edit/<int:pk>', views.ProductUpdate.as_view(), name='product_edit'),
    path('delete/<int:pk>', views.ProductDelete.as_view(), name='product_delete'),
]