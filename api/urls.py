from django.urls import path, include
from .views import *

urlpatterns = [
    path('v1/auth/login/',TokenLogin.as_view(),name="tokenLogin"),
    path('v1/auth/logout/',TokenLogout.as_view(),name="tokenLogout"),
    path('v1/products/',ProductData.as_view(),name="product"),
    path('v1/category/',CategoryData.as_view(),name="category"),
    path('v1/users/',UserData.as_view(),name="user"),


]