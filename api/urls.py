from django.contrib import admin
from django.urls import path, include
from .views import custom_user, category_detail, category, custom_user_detail, product, product_detail

urlpatterns = [
    path('users/', custom_user),
    path('users/<int:pk>/', custom_user_detail),
    path('category/', category),
    path('category/<int:pk>/', category_detail),
    path('product/', product),
    path('product/<int:pk>/', product_detail)
]