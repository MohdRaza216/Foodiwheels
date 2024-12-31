import re
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Message

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'phone', 'address', 'profile_picture']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'phone', 'desc']
        widgets = {
            'desc': forms.Textarea(attrs={'rows': 5}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Your Email'}),

        }
        error_messages = {
            'phone': {'invalid': 'Enter a valid phone number.'},
        }

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\d{10,12}$', phone):
            raise forms.ValidationError("Phone number must be 10-12 digits.")
        return phone
