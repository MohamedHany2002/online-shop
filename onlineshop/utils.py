import random
import string
from django.utils.text import slugify
# from shop.models import Product


def randomSlugGenerator(size=10):
    chars=string.ascii_lowercase+string.digits+string.ascii_uppercase
    return ''.join([random.choice(chars) for _ in range(size)])

def uniqueOrderId(instance):
    klass=instance.__class__
    order_id=randomSlugGenerator()
    qs=klass.objects.filter(order_id=order_id)
    if qs.exists():
        uniqueOrderId(instance)
    else:
        return order_id



def uniqueSlugGenerator(instance):
    generated_slug=randomSlugGenerator()
    generated_slug=slugify(instance.name)+'-'+generated_slug
    klass=instance.__class__
    qs=klass.objects.filter(slug=generated_slug)    
    if qs.exists():
        uniqueSlugGenerator(instance)
    else:
        return generated_slug
    
