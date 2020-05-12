
import string
import random
# from coupons.models import Coupon
def unique_code(instance):
    klass=instance.__class__
    tokens=string.ascii_lowercase+string.ascii_uppercase+string.digits
    # code = ""
    code=''.join([random.choice(tokens) for _ in range(10)])
    if not (klass.objects.filter(code=code).exists()):
        return code
    else:
        unique_code(instance)
# unique_code()
