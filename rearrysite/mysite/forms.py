from django import forms
from django.contrib.auth import get_user_model

class UserCreationForm(forms.ModelForm):
    password = forms.CharField()
    
    class Meta:
        model = get_user_model()
        fields = "email"
        
    def clean_password(self):
        password = self.cleaned_data.get["password"]
        return password
    