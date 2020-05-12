from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

address_choices=(('shipping','Shipping'),('billing','Billing'))

class guestuser(models.Model):
    email = models.EmailField()

class address(models.Model):
    address_type=models.CharField(max_length=120,choices=address_choices)
    address_line = models.CharField(max_length=120)
    address_line2 = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)


class userManager(BaseUserManager):
    def createUser(self,email,password,username=None,staff=False,active=True,admin=False):
        user_obj=self.Model.objects.create(email=email,password=password,username=username,staff=staff,active=active,admin=admin)
        return user_obj



class User(AbstractBaseUser):
    email = models.EmailField(unique=True,max_length=255)
    username = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    objects = userManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['email','password']

    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True
    
    def  has_module_perms(self,app_label):
        return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff





