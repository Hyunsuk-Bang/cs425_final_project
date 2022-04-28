from django.urls import path
from . import views
from product.views import *

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.home, name='home'),
    path('cart', views.cart, name = 'cart'),
    path('card', views.card, name = 'card'),
    path('address', views.address, name = 'address'),
    path('edit', views.edit, name = "edit"),
    path('new_card', views.add_card, name = "new_card"),
    path("new_address", views.add_address, name = "new_address"),
    path("<str:pid>/", views.product_detail, name = "product_detail"),
    path("cart/<str:p_id>/delete", views.cart_delete, name = "cart_delete"),
    path('cart/<str:p_id>/plus', views.cart_plus, name = 'cart_plus'),
    path('cart/<str:p_id>/minus', views.cart_minus, name = 'cart_minus')
]