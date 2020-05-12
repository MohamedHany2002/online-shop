from django.contrib import admin
from .models import Coupon
# Register your models here.

class CouponAdmin(admin.ModelAdmin):
    list_display=['code','discount','starts','ends']
    list_filter=['active','starts','ends']


admin.site.register(Coupon,CouponAdmin)
