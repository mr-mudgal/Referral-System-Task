from django import forms
from .models import UserRegistrationModel


class UserForm(forms.Form):
    full_name = forms.CharField(label="Full name *", max_length=100, required=True)
    email = forms.EmailField(label="Email *", required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True, label='Password *')
    referral_code = forms.CharField(required=False)

    class Meta:
        model = UserRegistrationModel
