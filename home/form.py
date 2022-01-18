from django import forms
from .models import User_Info
from .models import Reservation
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(forms.ModelForm):
    # username = forms.CharField(max_length=100)
    # password = forms.CharField(max_length=100)
    # email = forms.EmailField(max_length=100)

    class Meta:
        model = User_Info
        fields = ("username", "email", "password")


class LoginForm(AuthenticationForm):
    # password = forms.CharField(max_length=100)
    # email = forms.EmailField(max_length=100)

    class Meta:
        model = User_Info
        fields = ("username", "password")
        # fields = ("username", "email", "password")


class bookForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ("organizer", "date", "time", "room", "invitees", "title")
