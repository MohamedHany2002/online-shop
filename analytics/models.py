from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .signals import action_signal
from .utils import get_client_ip

# Create your models here.


class actions(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_actions',null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    contentType = models.ForeignKey(ContentType,on_delete=models.CASCADE,null=True,blank=True)
    object_id = models.PositiveIntegerField(null=True,blank=True)
    content_object = GenericForeignKey('contentType','object_id')
    client_ip = models.CharField(max_length=300)


def save_actions(sender,instance,request,**kwargs):
    ip = get_client_ip(request)
    if request.user.is_authenticated:
        actions.objects.create(user=request.user,content_object=instance,client_ip=ip)
    else:
        actions.objects.create(user=None,content_object=instance,client_ip=ip)

    print(request)
    print(sender)
    print(instance)
    print('got it')
    print(kwargs)
action_signal.connect(save_actions)