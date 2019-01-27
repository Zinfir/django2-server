from django import forms
import random, hashlib
from accounts.models import Account
from django.contrib.auth.forms import UserCreationForm


class BaseRegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = [
            'username',
            'password1',
            'email',
            'password2'
            ]
    
    def save(self, commit=True):
        obj = super(BaseRegistrationForm, self).save(commit=False)
        password = self.cleaned_data.get('password')

        obj.is_active=True
        #obj.is_active=False
        obj.set_password(password)

        if commit:
            obj.save()
        
        return obj


class Account_Form(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'phone',
            'avatar'
            ]
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'field_password'}),
            'email': forms.EmailInput(attrs={'class': 'field_email'}),
        }


class Registration_Form(forms.Form):
    username = forms.CharField(
        label='Login', max_length=150,
        widget=forms.widgets.TextInput(
            attrs={'class': 'field_username'}
        )
    )
    email = forms.CharField(
        max_length=150, required=True,
        widget=forms.widgets.EmailInput(
            attrs={'class': 'field_email'}
        )
    )
    password = forms.CharField(
        max_length=250,
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'field_password'}
        )
    )
    password_confirm = forms.CharField(
        max_length=250,
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'field_password'}
        )
    )


class Registration_Model_Form(forms.ModelForm):
    password_confirmed = forms.CharField(
        label='Confirmed password',
        required=True,
        widget=forms.PasswordInput()
    )


    class Meta:
        model = Account
        fields = [
            'username',
            'password',
            'email',
            ]
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'field_password'}),
            'email': forms.EmailInput(attrs={'class': 'field_email'}),
        }


    def clean_password_confirmed(self):
        password = self.cleaned_data.get('password')
        password_confirmed = self.cleaned_data.get('password_confirmed')

        if password and password_confirmed and password != password_confirmed:
            raise forms.ValidationError('Password is not confirmed')

        return self.cleaned_data

    
    def save(self, commit=True):
        obj = super(Registration_Model_Form, self).save(commit=False)
        password = self.cleaned_data.get('password')

        obj.is_active=False
        obj.set_password(password)

        if commit:
            obj.save()
        
        return obj

