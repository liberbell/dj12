from django import forms
from django.contrib.auth import get_user_model

class UserCreationForm(forms.ModelForm):
    password = forms.CharField()