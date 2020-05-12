

class Cart:
    def __init__(self,request):
        self.session = request.session
        cart=request.session.get('cart')
        if not cart:
            cart=request.session['cart']={}
        self.cart=cart

    def add(self,product,quantity=1):
        self.cart[str(product.id)]={'quantity':quantity,'price':str(product.price),'product':product}   
        # if update_quantity:
        #     self.cart[str(product.id)]['quantity']=quantity         
        # else:
        #     self.cart[str(product.id)]['quantity']+=quantity
        self.save()
        print(self.cart[str(product.id)])

    def save(self):
        self.session.modified=True  

    def clear(self):
        del self.session['cart']

