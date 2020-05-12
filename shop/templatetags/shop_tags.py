from django import template
from cart.models import cart
from django.shortcuts import get_object_or_404
from cart.models import cart_item


register=template.Library()


@register.filter
def checkcart(obj,request):
    
    #     mycart = get_object_or_404(cart,id=request.session.get('cart_id'))
    # else:
    #     mycart=cart.objects.create()
    #     request.session['cart_id']=mycart.id
    mycart = cart.objects.get(id=request.session['cart_id'])
    if mycart.cart_items.all():
        for cartitem in mycart.cart_items.all():
            if obj == cartitem.product:
                return True
    return False

@register.filter
def get_cart(request):
    return request

@register.filter
def checkProduct(obj,request):
    mycart,created=cart.objects.get_or_new(request,user=request.user)
    qs=cart_item.objects.filter(product=obj,cart=mycart)
    if qs.exists():
        return True
    return False





        
