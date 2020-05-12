from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save

# Create your models here.

class billingProfile(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

def save_billing(sender,**kwargs):
    if kwargs['created']:
        billingProfile(user=kwargs['instance'],email=kwargs['instance'])

post_save.connect(save_billing,User)


