from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save,post_save
from onlineshop.utils import uniqueSlugGenerator
from tags.models import Tag
from django.contrib.contenttypes.fields import GenericRelation
from analytics.models import actions
import csv

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def get_absolute_url(self):
        return reverse('products_category',args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=100,db_index=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,related_name='products')
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    slug = models.SlugField(blank=True,unique=True)
    available = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag,related_name='tags')
    product_actions= GenericRelation(actions)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail",args=[self.id,self.slug])
    @property
    def title(self):
        return self.name
# 

    class Meta:
        ordering=('created',)
        verbose_name='product'
        verbose_name_plural='products'
        index_together=(('id','slug'),)  # to improve performance for queries


def save_slug(sender,**kwargs):
    if not kwargs['instance'].slug:
        kwargs['instance'].slug=uniqueSlugGenerator(kwargs['instance'])
pre_save.connect(save_slug,sender=Product)