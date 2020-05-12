from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,reverse,redirect
from . models import Order
from cart.models import cart
from cart.context_processors import mycart
from Billingprofiles.models import billingProfile
from account.forms import login_form,guestform,addressform
from account.models import guestuser
from account.models import address
from .tasks import sending_message
from analytics.signals import action_signal
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import render_to_string
from django.http import HttpResponse
# import weasyprint
# Create your views here.

def checkout_success(request):
    return render(request,"order/success.html")

def checkout(request):
    order = None    
    mycart,created = cart.objects.get_or_new(request)
    if request.session['cart_count']==0:
        return HttpResponseRedirect(reverse('cart'))
    else:
        form=login_form()
        guest=guestform()
        address_form=addressform()
        obj=None
        if request.user.is_authenticated:
            obj,created=billingProfile.objects.get_or_create(user=request.user)
        elif request.session.get('guest_id'):
            guestobj=get_object_or_404(guestuser,id=request.session.get('guest_id'))
            obj,created=billingProfile.objects.get_or_create(email=guestobj.email)
        else:
            pass
        if obj:
            myoldones=Order.objects.filter(cart=mycart).exclude(billingprofile=obj)
            print(myoldones)
            myoldones.delete()
            print(Order.objects.filter(cart=mycart))
            order,ord=Order.objects.get_or_create(cart=mycart,billingprofile=obj)
            if request.session.get('shipping') is not None:
                order.shipping_address=address.objects.get(id=request.session.get('shipping'))
                order.save()
                del request.session['shipping']
            elif request.session.get('billing'):
                order.billing_address=address.objects.get(id=request.session.get('billing'))
                order.save()
                del request.session['billing']
            print('dfd',order)
        if request.method=='POST':
            # check order complete 
            print(order.cart,order.billingprofile,order)
            if order.check_complete():
                request.session['order_id']=order.id
                sending_message.delay(order.id)
                return HttpResponseRedirect(reverse('process'))
            else:
                print('incomplete order')
        klass=order.__class__
        print(action_signal)
        action_signal.send(klass,instance=order,request=request)
        return render(request,"order/checkout.html",{'order':order,'loginform':login_form,'guestform':guest,'billingprofile':obj,'addressform':address_form})

def go(request):
    print.delay()
    return render(request,"ok.html")

@staff_member_required
def order_detail(request,order_id):
    order=get_object_or_404(Order,id=order_id)
    return render(request,"admin/orders/order/detail.html",{'order':order})

# working but cairo package not working on windows x86




# @staff_member_required
# def print_to_pdf(request,id):
#     order=get_object_or_404(Order,id=id)
#     html = render_to_string('order/pdf.html',{'order':order})
#     pdf = render_to_pdf('order/pdf.html',{'order':order})
#     response=HttpResponse(content_type='application/pdf')
#     # response['Content-Disposition']='filename="order_{}.pdf"'.format(order.id)
#     # weasyprint.HTML(string=html).write_pdf(response)
#     return response
