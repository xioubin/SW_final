from importlib.resources import contents
import re
from django.contrib import auth
from django.shortcuts import render, redirect
from .models import Reservation, User_Info, ErrorReport
from .form import RegisterForm, LoginForm, bookForm, forgetForm, IndexDateForm
from django.contrib import messages
from django.views.generic.edit import FormView

from django.core.mail import send_mail
from django.conf import settings
import random
import string
# Create your views here.

# time_choices = ['8:00-9:00', '9:00-10:00', '10:00-11:00',
#                 '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00', ]
# room_choices = [1, 2, 3, 4, 5]


def index(request):
    form = IndexDateForm()

    if request.method == "POST":
        form = IndexDateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            host_reservations = Reservation.objects.filter(
                date=date)
            print(host_reservations)
            # print(date)
            return redirect('/home/')
        else:
            print(form.errors)

    context = {}
    context['subtitle'] = '借用情形查詢'
    context['time_choices'] = Reservation.TIME_CHOICES
    context['room_choices'] = Reservation.ROOM_CHOICES
    context['form'] = form

    return render(request, 'index.html', context=context)


def book(request):
    if request.method == "POST":
        form = bookForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            # auth.login(request, user)
            return redirect('/home/')
    form = bookForm(user=request.user)
    context = {}
    context['subtitle'] = '借用'
    context['form'] = form
    return render(request, 'book.html', context)


def modify(request):
    context = {}
    context['subtitle'] = '借用'
    return render(request, 'modify.html', context)


def comfirm(request):
    return render(request, 'comfirm.html')


def forget(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    if request.method == "POST":
        form = forgetForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            count = User_Info.objects.filter(email=email).count()
            if count == 1:
                random_password = ''.join(random.sample(
                    string.ascii_letters + string.digits, 8))
                User_Info.objects.filter(email=email).update(
                    password=random_password)

                # send_mail
                subject = "Password reset notification"
                message = "your password is changed to " + random_password
                sender = settings.EMAIL_HOST_USER
                recipient = [email]
                send_mail(
                    subject,
                    message,
                    sender,
                    recipient
                )
                return redirect('/home/login/')
            else:
                print("this email address hasn't been registered.")
    form = forgetForm()
    context = {}
    context['subtitle'] = '忘記密碼'
    context['form'] = form
    return render(request, 'forget.html', context)


def participants(request):
    return render(request, 'participants.html')


def records(request):
    if request.user.is_authenticated:
        # user_filter = request.user
        host_reservations = Reservation.objects.filter(organizer=request.user)
        invited_reservations = Reservation.objects.filter(
            invitees=request.user)
    else:
        print('non user')
        messages.error(
            request, "Unsuccessful user_filter.")
    context = {}
    context['subtitle'] = '借用記錄查詢'
    context['host_reservations'] = host_reservations
    context['invited_reservations'] = invited_reservations

    return render(request, 'records.html', context=context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            text = 'Hi! ' + form.cleaned_data.get(
                'username') + '\nYou are successfully register booking system. Please remember your account and password.'
            mail = form.cleaned_data.get('email')
            send_mail('註冊成功通知', text, None, [mail])
            auth.login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('/home/')
        print(form.errors)
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()
    context = {}
    context['subtitle'] = '註冊'
    context['form'] = form
    return render(request, 'register.html', context)


def report(request):
    print(request)
    if request.method == "POST":
        print("report")
        content = request.POST['content']
        unit = ErrorReport.objects.create(content=content)
        unit.save()
    context = {}
    context['subtitle'] = '錯誤回報'
    return render(request, 'report.html', context=context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    if request.method == "POST":
        print('login')

        form = LoginForm(data=request.POST)
        if form.is_valid():
            print('login1')

            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user_check = User_Info.objects.get(email=email)
            print(password, user_check.password)

            user = auth.authenticate(email=email, password=password)
            messages.success(request, "Login successful.")
            if user is not None and user.is_active:
                print('login2')

                auth.login(request, user)
                return redirect('/home/')
            else:
                print(user)
                messages.error(request, 'user not found')
        else:
            print(form.errors)
            print('form invalid')
            messages.error(
                request, "Unsuccessful registration. Invalid information.")

    form = LoginForm()
    context = {}
    context['subtitle'] = '登入'
    context['form'] = form
    return render(request, 'login.html', context)


def user_logout(request):
    auth.logout(request)
    return redirect('/home/')
