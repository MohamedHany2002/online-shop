from django.shortcuts import render,HttpResponseRedirect,redirect,get_object_or_404,reverse
from shop.models import Product
from .cart import Cart
from .models import cart,cart_item
from decimal import Decimal
from django.http import JsonResponse
from .serializers import cartSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from coupons.forms import codeForm
from analytics.signals import action_signal

# Create your views here.

def viewCart(request):
    mycart,created=cart.objects.get_or_new(request,user=request.user)
    if mycart.user is None and request.user.is_authenticated:
        mycart.user=request.user
        mycart.save()
    subtotal=0
    if mycart.cart_items.all():
        for item in mycart.cart_items.all():
            subtotal+=item.product.price*Decimal(item.quantity)
            item.item_total=subtotal
        mycart.total=subtotal - mycart.discount
        mycart.save()
    klass=mycart.__class__
    print(action_signal)
    action_signal.send(klass,instance=mycart,request=request)
    form=codeForm()
    return render(request,"cart/cartview.html",{'cart':mycart,'form':form})

def update(request):
    print('got it')
    if request.POST.get('quantity'):
        mycartitem=get_object_or_404(cart_item,id=request.POST['item_id'])
        mycartitem.quantity=request.POST.get('quantity')
        mycartitem.item_total=mycartitem.product.price*Decimal(mycartitem.quantity)
        mycartitem.save()
        return HttpResponseRedirect(reverse('cart'))
    print('here')
    myproduct=get_object_or_404(Product,id=request.POST['id'])
    mycart,created=cart.objects.get_or_new(request,user=request.user)
    print(mycart)
    cartitem,created=cart_item.objects.get_or_create(cart=mycart,product=myproduct)
    print(mycart.cart_items.all())
    if not created:
        added=False
        mycart.cart_items.remove(cartitem)
    else:
        added = True
        cartitem.item_total=cartitem.product.price
        cartitem.save()
    request.session['cart_count']=mycart.cart_items.count()
    cart_count = mycart.cart_items.count()
    return JsonResponse({'added':added,'removed':not added,'count':cart_count})
    # return HttpResponseRedirect(reverse('cart'))

def edit(request,id):
    print(request.POST['quantity'])
    mycart,created=cart.objects.get_or_new(request)
    item=get_object_or_404(cart_item,id=id)
    if request.POST.get('quantity'):
        item.quantity=request.POST['quantity']
        q=request.POST['quantity']
        q=Decimal(q)
        item.item_total=q*item.product.price
        item.save()
    return HttpResponseRedirect(reverse('cart'))


@api_view(('GET',))
def cartApi(request):
    mycart,created=cart.objects.get_or_new(request)
    cartItems = mycart.cart_items.all()
    items = cartSerializer(cartItems,many=True)
    return Response(items.data)


def remove_cart(request):
    del request.session['cart_id']
    return HttpResponseRedirect(reverse('cart'))

def apicart(request):
    mycart,created=cart.objects.get_or_new(request)
    items=[{'price':x.product.price,'name':x.product.title} for x in  mycart.cart_items.all()]
    return JsonResponse({'items':items})


