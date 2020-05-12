from django.db import models
from django.db.models.signals import pre_save,post_save
from onlineshop.utils import uniqueOrderId
from math import fsum
from decimal import Decimal
from django.shortcuts import reverse
from Billingprofiles.models import billingProfile
from cart.models import cart
from account.models import address
from analytics.models import actions
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.


status_choiced=(('created','Created'),('paid','Paid'),('shipped','Shipped'),('refunded','Refunded'))

class Order(models.Model):
    cart = models.ForeignKey(cart,on_delete=models.CASCADE,related_name='orders')
    order_id = models.CharField(max_length=120,blank=True)
    shipping_total = models.DecimalField(default=5.99,decimal_places=2,max_digits=10)
    order_total = models.DecimalField(default=0.00,decimal_places=2,max_digits=10)
    status = models.CharField(max_length=120,choices=status_choiced,default='created')
    billingprofile = models.ForeignKey(billingProfile,on_delete=models.CASCADE,null=True,blank=True)
    billing_address = models.ForeignKey(address,on_delete=models.CASCADE,related_name='billing_orders',null=True,blank=True)
    shipping_address = models.ForeignKey(address,on_delete=models.CASCADE,related_name='shipping_orders',null=True,blank=True)
    action =GenericRelation(actions)
    transaction_id = models.CharField(max_length=100,null=True,blank=True)

    def get_absolute_url(self):
        return reverse('checkout')

    def calc_total(self):
        mytotal=Decimal(self.shipping_total) + self.cart.total
        formated_total=format(mytotal,'.2f')
        self.order_total=formated_total
        # self.save()
    
    def check_complete(self):
        if self.cart and self.billingprofile  and self.cart.total>0.00:
            if self.shipping_address or self.billing_address:
                self.status = 'paid'
                self.save()
                return True
        return False

def editOrder(sender,**kwargs):
    if not kwargs['created']:
        qs=Order.objects.filter(cart=kwargs['instance'])
        if qs.exists():
            for order in kwargs['instance'].orders.all():
                order.order_total=kwargs['instance'].total
                order.save()
post_save.connect(editOrder,cart)



def save_orderId(sender,**kwargs):
    # if kwargs['created']:
    kwargs['instance'].order_id=uniqueOrderId(kwargs['instance'])
    kwargs['instance'].calc_total()
pre_save.connect(save_orderId,Order)

# def save_order_total(sender,**kwargs):
#     kwargs['instance'].calc_total()
#     # kwargs['instance'].save()
# post_save.connect(save_order_total,sender=Order)

# unique slug generator .. id unique generator .. tags 