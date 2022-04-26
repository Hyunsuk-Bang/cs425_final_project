from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main),
    path('<str:p_id>', views.product_detail),
]