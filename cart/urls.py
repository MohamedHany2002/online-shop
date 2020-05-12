
from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.viewCart,name='cart'),
    path('edit/<int:id>', views.edit,name='edit'),
    path('update/', views.update,name='update'),
    path('remove_cart/', views.remove_cart,name='clear'),
    path('cart/api/', views.cartApi,name='cart_api'),
    path('apiCart/', views.apicart,name='api_cart'),
]   
