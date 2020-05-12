from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import login_form,addressform
from .models import guestuser
# Create your views here.

def user_login(request):
    if request.method=='POST':
        loginform=login_form(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        url = request.POST['url']
        user=authenticate(username=username,password=password)
        # remove guest_id
        if request.session.get('guest_id'):
            del request.session['guest_id']
        print(user)
        if user is not None:
            login(request,user)
            if url:
                return redirect(url)
            else:
                return HttpResponseRedirect(reverse('products'))
        else:
            return render(request,"account/login.html",{'loginform':loginform})

    else:
        loginform=login_form()
        return render(request,"account/login.html",{'loginform':loginform}) 

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def guestgrap(request):
    if request.method=='POST':
        loginform=login_form(request.POST)
        email=request.POST['email']
        if email is not None:
            guest,created=guestuser.objects.get_or_create(email=email)
            request.session['guest_id']=guest.id
            return HttpResponseRedirect(reverse('checkout'))
    else:
        loginform=login_form()
        return render(request,"account/login.html",{'loginform':loginform}) 

def save_address(request):
    if request.method=='POST':
        form = addressform(request.POST)
        if form.is_valid():
            new_address=form.save()
        if new_address.address_type=='shipping':
            request.session['shipping']=new_address.id
        else:
            request.session['billing']=new_address.id
        if request.POST['url']:
            return redirect(request.POST['url'])
        else:
            return HttpResponseRedirect(reverse('checkout'))
        
