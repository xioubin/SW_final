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
    def __init__(self, *args, user=None,time=None,room=None,date=None, **kwargs):
        super(bookForm, self).__init__(*args, **kwargs)
        print(time,"1")
        if user is not None:
            self.fields['organizer'].initial = user
        if time is not None:
            print(time,"2")
            if time=="8-9":
                timeid = 0
            if time=="9-10":
                timeid = 1
            if time=="10-11":
                timeid = 2     
            if time=="11-12":
                timeid = 3
            if time=="12-13":
                timeid = 4
            if time=="13-14":
                timeid = 5
            if time=="14-15":
                timeid = 6
            if time=="15-16":
                timeid = 7
            if time=="16-17":
                timeid = 8
            self.fields['time'].initial = timeid
        if room is not None:
            if room =="(0, 'ROOM 1')":
                roomid=0
            if room =="(1, 'ROOM 2')":
                roomid=1
            if room =="(2, 'ROOM 3')":
                roomid=2
            if room =="(3, 'ROOM 4')":
                roomid=3
            if room =="(4, 'ROOM 5')":
                roomid=4
            self.fields['room'].initial = roomid
        if date is not None:
            self.fields['date'].initial = date

    date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date'}))
    invitees = forms.CheckboxSelectMultiple()
    # shift

    class Meta:
        model = Reservation
        fields = ("organizer", "date", "time", "room", "invitees", "title")


class ModifyForm(forms.ModelForm):

    def __init__(self, *args, user=None, **kwargs):
        super(ModifyForm, self).__init__(*args, **kwargs)
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


class IndexDateForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date'}))

    # class Meta:
    #     model = Reservation
    #     fields = ("date")
