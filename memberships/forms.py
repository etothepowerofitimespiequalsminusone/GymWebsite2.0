from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    personal_number = forms.CharField(min_length=12,max_length=12)
    phone_number = forms.IntegerField()

    class Meta:
        model = User
        fields = ['name','surname','email','identity_number','phone_number','password']
