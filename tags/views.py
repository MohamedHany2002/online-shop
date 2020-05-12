from django.shortcuts import render,get_object_or_404
from .models import Tag

# Create your views here.


def searchbytag(request,name):
    tag=get_object_or_404(Tag,name=name)
    products = tag.product.all()
    return render(request,'search.html',{'products':products,'tag':tag})
