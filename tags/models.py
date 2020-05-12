from django.db import models
# Create your models here.
from django.db.models.signals import pre_save
from onlineshop.utils import uniqueSlugGenerator


class Tag(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True,blank=True)

    def __str__(self):
        return self.name

def save_slug(sender,**kwargs):
    if not kwargs['instance'].slug:
        kwargs['instance'].slug=uniqueSlugGenerator(kwargs['instance'])
pre_save.connect(save_slug,sender=Tag)
