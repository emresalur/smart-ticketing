#coding:utf-8
from django import forms
from accounts.models import UserProfile
import re
import sys
import os

#login form
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "username", "required": "required","id":"user","name":"username"}),
                              max_length=100,error_messages={"required": "username:Can not be empty",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "password", "required": "required","id":"password","name":"password"}),
                              max_length=200,error_messages={"required": "password:Can not be empty",})

#registration form
class RegForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "username", "required": "required",}),
                              max_length=50,error_messages={"required": "Username can not be empty",})
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "email", "required": "required",}),
                              max_length=50,error_messages={"required": "Email cannot be empty",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "password", "required": "required",}),
                              max_length=20,error_messages={"required": "password can not be blank",})
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "confirm password", "required": "required",}),
                              max_length=20,error_messages={"required": "password can not be empty",})

    def clean(self):
        if not self.is_valid():
             raise forms.ValidationError('All fields are required')
        elif self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise forms.ValidationError('The passwords entered twice does not match')
        else:
            cleaned_data = super(RegForm,self).clean()
        username = self.cleaned_data['username']
        is_email_exist = UserProfile.objects.filter(email=username).exists()
        is_username_exist = UserProfile.objects.filter(username=username).exists()
        if is_username_exist or is_email_exist:
            raise forms.ValidationError(u"The account has already been registered")

        return cleaned_data

#registration form
class RegPhoneForm(forms.Form):
    # username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "username", "required": "required",}),
    #                           max_length=50,error_messages={"required": "Username can not be empty",})
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "mobile phone", "required": "required",}),
                              max_length=50,error_messages={"required": "Phone cannot be empty",})
    # email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "Mail", }),
    #                          max_length=50, )
    # password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "password", "required": "required",}),
    #                           max_length=20,error_messages={"required": "password can not be blank",})
    # confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm password", "required": "required",}),
    #                           max_length=20,error_messages={"required": "Confirmed password can not be blank",})

    def clean(self):
        if not self.is_valid():
             raise forms.ValidationError('All fields are required')
        else:
            cleaned_data = super(RegPhoneForm,self).clean()
        phone = self.cleaned_data['phone']
        is_mobile_exist = UserProfile.objects.filter(mobile=phone).exists()
        if is_mobile_exist:
            raise forms.ValidationError(u"The phone number has already been registered")
        p2 = r'^0\d{2,3}\d{7,8}$|^1[3578]\d{9}$|^147\d{8}'
        phonematch = re.findall(r'^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}', phone)
        if len(phonematch) == 0 or phonematch==None or phonematch=="" :
            raise forms.ValidationError(u"The phone number is in the wrong format")
        return cleaned_data


