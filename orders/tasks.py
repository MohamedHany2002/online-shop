from celery import task
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from .models import Order

@task
def sending_message(order_id):
    ordered_order=get_object_or_404(Order,id=order_id)
    subject='ordering successfully an order'
    message='you have ordered an order Id number {} by this mail {}'.format(ordered_order.order_id,ordered_order.billingprofile.email)
    sent_mail=send_mail(subject,message,'goldenhany94@gmail.com',['hanygolden94@gmail.com'])
    return sent_mail


    