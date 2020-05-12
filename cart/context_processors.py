from .models import cart

def mycart(request):
    mycart,created = cart.objects.get_or_new(request,user=request.user)
    return {'global_cart':mycart}