
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login,name='login'),
    path('logout/', views.user_logout,name='logout'),
    path('guest/', views.guestgrap,name='guest'),
    path('address/', views.save_address,name='address'),
]   
