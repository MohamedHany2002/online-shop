from django.shortcuts import render,get_object_or_404,redirect
from orders.tasks import sending_message
from orders.models import Order
import braintree


# Create your views here.

def process_payments(request):
    order = get_object_or_404(Order,id=request.session.get('order_id',None))
    if request.method=='POST':
        print('here')
        nonce = request.POST.get('payment_method_nonce',None)
        print(nonce,'sdfdsf')
        result=braintree.Transaction.sale({
        'amount':'{:.2f}'.format(order.order_total),
        'payment_method_nonce':nonce,
        'options':{
        'submit_for_settlement':True
        }    
        }
        )
        if result.is_success:
            order.status='paid'
            order.transaction_id=result.transaction.id
            order.save()
            del request.session['cart_id']
            # send message with attatched pdf file
            # watch this again
            return redirect('done')
        else:
            return redirect('canceled')
    else:
        client_token=braintree.ClientToken.generate()
    return render(request,"payment/process.html",{'order':order,'client_token':client_token})

def done(request):
    return render(request,"payment/done.html")
    
def canceled(request):
    return render(request,"payment/canceled.html")
