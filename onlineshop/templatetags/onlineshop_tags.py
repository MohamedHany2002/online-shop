from django import template
from cart.models import cart
from django.shortcuts import get_object_or_404


register=template.Library()


@register.filter
def checkcart(obj,request):
    print(request.user)
    #     mycart = get_object_or_404(cart,id=request.session.get('cart_id'))
    # else:
    #     mycart=cart.objects.create()
    #     request.session['cart_id']=mycart.id
    if request.session.get('cart_id'):
        mycart = cart.objects.get(id=request.session.get('cart_id'))
        if mycart is not None:
            qs=mycart.cart_items.filter(product=obj)
            if qs.exists():
                return True
            else:
                return False

    #         for cartitem in mycart.cart_items.all():
    #             if obj == cartitem.product:
    #                 print("exist in cart")
    #                 return "lol"
    # return request.session['cart_id']
    
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
        
