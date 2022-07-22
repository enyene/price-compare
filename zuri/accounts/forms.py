from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.forms import ModelForm

from .models import User

class CaseInsensitiveUsernameMixin(forms.Form):
    """
    Disallow a username with a case-insensitive match of existing usernames.
    """

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if get_user_model().objects.filter(username__iexact=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError((u'The username ‘{}’ is already in use.'.format(str(username).casefold())))
        return username

class RegisterForm(UserCreationForm,CaseInsensitiveUsernameMixin):
    '''
    User registration form 
    fields [username,email and password]
    used with register view
    
    '''

    # id templates for css customization
    error_css_class = 'error'
    required_css_class = 'required'

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

class LoginForm(forms.form):
    '''
    user login form with fields username and password 
    used with login views and template
    '''
    username = forms.CharField(widget=forms.TextInput(attrs={}),label='Username')
    password = forms.CharField(widget=forms.PasswordInput,label='Password')