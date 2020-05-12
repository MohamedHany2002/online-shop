from django.db import models
from shop.models import Product
from django.db.models.signals import pre_save,post_save,m2m_changed,pre_init,post_init
from django.contrib.auth.models import User
# from orders.models import Order
from django.shortcuts import get_object_or_404

# Create your models here.

class cartManager(models.Manager):
    
    def get_or_new(self,request,user=None):
        print("this",user)
        created = False
        get_cart=request.session.get('cart_id')
        if not get_cart:
            if user is not None and user.is_authenticated:
                mycart=self.model.objects.create(user=user)
                # print(mycart.user)
            else:
                mycart=self.model.objects.create()                
            request.session['cart_id']=mycart.id
            created = True
        else:
            mycart=get_object_or_404(cart,id=request.session.get('cart_id'))
            print(mycart.id)
        print(created)
        return mycart,created


class cart(models.Model):
    total = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='user_carts')
    discount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    objects=cartManager()

    @property
    def getcount(self):
        return self.cart_items.count()>0



class cart_item(models.Model):
    cart = models.ForeignKey(cart,on_delete=models.CASCADE,related_name='cart_items',null=True,blank=True)
    product = models.ForeignKey(Product,related_name='cart_items',blank=True,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    item_total = models.DecimalField(max_digits=10,decimal_places=2,default=0)



