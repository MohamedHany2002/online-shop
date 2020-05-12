
from django.urls import path
from . import views

urlpatterns = [
    path('process/',views.process_payments,name='process'),
    path('done/',views.done,name='done'),
    path('canceled/',views.canceled,name='canceled')
]
