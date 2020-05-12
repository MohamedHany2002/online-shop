from django.contrib import admin
from . models import guestuser
from .models  import User
# from .forms import CustomUserChangeForm,CustomUserCreationForm
# from django.contrib.auth.admin import UserAdmin


# Register your models here.

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = User
#     list_display = ['email', 'username',]

# admin.site.register(User, CustomUserAdmin) 

admin.site.register(guestuser)