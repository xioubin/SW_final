from django import forms
from .models import User_Info
<<<<<<< HEAD
=======
from .models import Login_Info
>>>>>>> 5278c158db3a161f8edbcf8171c41258e6b39a34


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

<<<<<<< HEAD
=======
class LoginForm(forms.ModelForm):   
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    
    class Meta:
        model = Login_Info
        fields = ("username", "password")
>>>>>>> main
>>>>>>> 5278c158db3a161f8edbcf8171c41258e6b39a34
