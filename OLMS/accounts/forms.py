# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, required=True, help_text="Enter your full name")
    profile_picture = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'full_name', 'profile_picture')

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'email', 'profile_picture']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-input'}),
        }

# No Changes Applied, Using The Built-in Password Change Form 
class CustomPasswordChangeForm(PasswordChangeForm):
    pass