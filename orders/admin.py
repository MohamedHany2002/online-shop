from django.contrib import admin
from .models import Order
import csv
from import_export.admin import ImportExportModelAdmin
from django.urls import reverse
from django.utils.safestring import mark_safe
# Register your models here.


class OrderAdmin(admin.ModelAdmin): 
    list_display = ['order_id','order_detail'] 

@admin.register(Order) 
class OrderCsv(ImportExportModelAdmin):
    pass


def order_detail(obj):
    return mark_safe('<a herf="{}">View</a>'.format(reverse('order_detail',[obj.id]))) 


# pdf coloumn
# def order_detail(obj):
#     return mark_safe('<a herf="{}">View</a>'.format(reverse('pdf',[obj.id]))) 

