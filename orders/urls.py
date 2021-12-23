from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login",views.log_in, name= "login"),
    path("logout",views.log_out, name="logout"),
    path('addtocart/', views.addtocart, name="addtocart"),
    path('addtocart/<str:id>', views.addtocart, name="edit"),
    path('cart', views.cart, name="cart"),
    path('cart/<user>', views.cart, name="cartu"),
    path('remove/<str:id>', views.remove, name="remove"),
    path('remove/', views.remove, name="removeall"),

]
