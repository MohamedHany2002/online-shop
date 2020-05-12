from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from .utils import unique_code
# Create your models here.

from django.db.models.signals import pre_save,post_save
from django.utils import timezone

class Coupon(models.Model):
    code  = models.CharField(max_length=150,unique=True,blank=True)
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    starts = models.DateTimeField()
    ends = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

    def is_valid(self):
        if Coupon.objects.filter(self__starts__lte=timezone.now(),self__ends__gte=timezone.now()).exists():
            self.active = True
        else:
            self.active=False

def save_code(sender,**kwargs):
    c=Coupon.objects.filter(id=kwargs['instance'].id)
    if not c.exists():
        code=unique_code(kwargs['instance'])
        kwargs['instance'].code=code
pre_save.connect(save_code,sender=Coupon)


