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

# should be no organizer => organizer should and in view by request.user


class bookForm(forms.ModelForm):
    def __init__(self, *args, user=None, time=None, room=None, date=None, **kwargs):
        super(bookForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['organizer'].initial = user
        if time is not None:
            self.fields['time'].initial = time
        if room is not None:
            self.fields['room'].initial = room
        if date is not None:
            self.fields['date'].initial = date

    date = forms.DateField(label='date', widget=forms.DateInput(attrs={
        'type': 'date'}))
    invitees = forms.CheckboxSelectMultiple()
    # shift

    class Meta:
        model = Reservation
        fields = ("organizer", "date", "time", "room", "invitees", "title")


class ModifyForm(forms.ModelForm):

    def __init__(self, *args, user=None, date=None, **kwargs):
        super(ModifyForm, self).__init__(*args, **kwargs)
        if date is not None:
            self.fields['date'].initial = date
    date = forms.DateField(label='date', widget=forms.DateInput(attrs={
        'type': 'date'}))
    invitees = forms.CheckboxSelectMultiple()
    # shift

    class Meta:
        model = Reservation
        fields = ("organizer", "date", "time", "room", "invitees", "title")


class forgetForm(forms.Form):
    email = forms.EmailField()


class IndexDateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date'}))

    # class Meta:
    #     model = Reservation
    #     fields = ("date")
