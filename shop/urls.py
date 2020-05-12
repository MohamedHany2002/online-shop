
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search,name='search'),
    path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
    path('', views.listProduct,name='products'),
    path('exp/', views.exp,name='exp'),
    path('<slug:category_slug>/', views.listProduct,name='products_category'),
]
