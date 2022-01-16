
from contextlib import redirect_stderr
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .models import Reservation
# Create your views here.

time_choices = ['8:00-9:00', '9:00-10:00', '10:00-11:00',
                '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00', ]
room_choices = [1, 2, 3, 4, 5]


def index(request):
    context = {}
    context['subtitle'] = '借用情形查詢'
    context['time_choices'] = Reservation.TIME_CHOICES
    context['room_choices'] = Reservation.ROOM_CHOICES

    return render(request, 'index.html', context=context)


def book(request):
    return render(request, 'book.html')


def comfirm(request):
    return render(request, 'comfirm.html')


def forget(request):
    return render(request, 'forget.html')


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


# def home(request):
#     context={}
#     context['timechoices']=time_choices
#     context['subtitle'] = '借用情形查詢'
#     return render(request, 'home.html', context=context)


def participants(request):
    return render(request, 'participants.html')


def records(request):
    return render(request, 'records.html')


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/login')
    else:
        form = UserCreationForm()
    context = {}
    context['subtitle'] = '註冊'
    context['form'] = form
    return render(request, 'register.html', context)


def report(request):
    context = {}
    context['subtitle'] = '錯誤回報'
    return render(request, 'report.html', context=context)


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/home/')
    else:
        return render(request, 'login.html', locals())


def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')
