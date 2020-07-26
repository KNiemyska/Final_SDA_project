from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    phone_number=forms.CharField(label='numer telefonu',max_length=9)
    usersurname=forms.CharField(label='Nazwisko')

    class Meta:
        model=User
        fields = ['username','usersurname','email','phone_number', 'password1','password2']

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)