from django import forms
from .models import User_Info
from .models import Login_Info


# Create your forms here.

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User_Info
        fields = ("username", "email", "password")

<<<<<<< HEAD
=======
class LoginForm(forms.ModelForm):   
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    
    class Meta:
        model = Login_Info
        fields = ("username", "password")
>>>>>>> main
