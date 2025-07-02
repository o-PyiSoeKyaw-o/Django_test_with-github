from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('category/list/', views.CategoryList),
    path('category/create/', views.CategoryCreate),
    path('category/update/<int:id>/', views.CategoryUpdate),
    path('category/delete/<int:id>/', views.CategoryDelete),

    # Product
    path('product/list/', views.ProductList),
    path('product/create/', views.ProductCreate),
    path('product/update/<int:id>/', views.ProductUpdate),
    path('product/delete/<int:id>/', views.ProductDelete),
]