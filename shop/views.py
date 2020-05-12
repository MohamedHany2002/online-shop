from django.shortcuts import render,get_object_or_404
from .models import Category,Product
from cart.models import cart
from django.db.models import Q
from tags.models import Tag
from analytics.signals import action_signal
import celery
import djcelery
import kombu
import redis
from . import tasks
# Create your views here.

def listProduct(request,category_slug=None):
    tasks.printhello.delay()
    # print(x,'sdfsfds')
    print(celery)
    print(redis)
    print(djcelery)
    products=Product.objects.filter(available=True)
    category=None
    categories=Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    
    return render(request,"products/home.html",{'products':products,'category':category,'categories':categories})

def product_detail(request,id,slug):
    if request.session.get('cart_id'):
        mycart = get_object_or_404(cart,id=request.session.get('cart_id'))
    else:
        mycart=cart.objects.create()
        request.session['cart_id']=mycart.id
    product=get_object_or_404(Product,id=id,slug=slug)
    klass=product.__class__
    print(action_signal)
    action_signal.send(klass,instance=product,request=request)
    return render(request,"products/detail.html",{'product':product,'cart':mycart})


def search(request):
    name='blue'
    # tagss = Tag.objects.filter(name__icontains=name)
    # print(tagss)
    products=Product.objects.filter(Q(tags__name__icontains=name)|Q(name=name)).distinct()
    print(products)
    context={'products':products}
    return render(request,"search.html",context)

def exp(request):
    x=tasks.printhello()
    print(x)
    return render(request,"index.html")

