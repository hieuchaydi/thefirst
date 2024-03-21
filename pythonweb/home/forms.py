import re
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Account', max_length=20)  
    email = forms.EmailField(label='Email') 
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password1 = forms.CharField(label='Enter password again', widget=forms.PasswordInput()) 
    
    def clean_password1(self):
        password = self.cleaned_data['password']  
        password1 = self.cleaned_data['password1']  
        if password != password1:
            raise forms.ValidationError("Passwords do not match")
        return password1
    
    def clean_username(self):
        username = self.cleaned_data['username']  
        if not re.search(r'^\w+$', username): 
            raise forms.ValidationError("Username should only contain letters, digits, and underscores.")
        try:
            User.objects.get(username=username)
            raise forms.ValidationError("Account already exists")
        except ObjectDoesNotExist:
            return username
    
    def save(self):
        User.objects.create_user(username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password'])  # Corrected capitalization of cleaned_data
