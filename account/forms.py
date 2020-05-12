from django import forms
from .models import address
from .models import User

class login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class guestform(forms.Form):
    email = forms.EmailField()


class addressform(forms.ModelForm):
    class Meta:
        model = address
        fields=['address_type','address_line','address_line2','city','state','country','postal_code']


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email')


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email')