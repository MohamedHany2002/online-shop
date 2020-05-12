
from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.applyCoupon,name='coupon'),
]   
