from django import forms
from .models import User_Info


class RegisterForm(forms.ModelForm):
    # username = forms.CharField(max_length=100)
    # password = forms.CharField(max_length=100)
    # email = forms.EmailField(max_length=100)

    class Meta:
        model = User_Info
        fields = ("username", "email", "password")


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)

    class Meta:
        model = User_Info
        fields = ("username", "password")


# class bookForm(forms.ModelForm):
#     room = forms.CharField(max_length=10)
#     time = forms.CharField(max_length=20)
#     participant = forms.CharField(max_length=100)

#     class Meta:
#         model = Book_Info
#         fields = ("room", "time", "participant")
