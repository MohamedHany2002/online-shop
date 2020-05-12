
from django.urls import path,include
from . import views

urlpatterns = [
    path('checkout/', views.checkout,name='checkout'),
    path('success/', views.checkout_success,name='success'),
    path('admin/order/<int:order_id>/', views.order_detail,name='order_detail'),
    path('go/', views.go,name='go'),
    # path('pdf/', views.print_to_pdf,name='order_pdf'),
]
