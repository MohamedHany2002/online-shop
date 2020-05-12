from django.shortcuts import render,reverse,HttpResponse,redirect
from .forms import codeForm
from .models import Coupon
from django.utils import timezone
from django.views.decorators.http import require_POST
from cart.models import cart
from decimal import Decimal
# Create your views here.

# @require_POST
def applyCoupon(request):
    if request.method=='POST':
        print('sdf')
        form=codeForm(request.POST)
        if form.is_valid():
            print('gggg')
            code=request.POST.get('code',None)
            print('ggggg')
            qs = Coupon.objects.filter(code=code)
            print(qs)
            if qs.exists():
                obj = qs.first()
                discount=obj.discount
                mycart,created=cart.objects.get_or_new(request)
                mycart.discount = Decimal(discount/100)
                mycart.save()
                print(mycart.discount)
        return redirect('cart')       