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

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(user.password)  # set password properly before commit
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class bookForm(forms.ModelForm):
    def __init__(self, *args, user=None, **kwargs):
        super(bookForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['organizer'].initial = user.email
    organizer = forms.CharField()
    date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date'}))
    invitees = forms.CheckboxSelectMultiple()
    # shift

    class Meta:
        model = Reservation
        fields = ("organizer", "date", "time", "room", "invitees", "title")


class forgetForm(forms.Form):
    email = forms.EmailField()
