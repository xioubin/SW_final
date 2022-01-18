from django.contrib import auth
from django.shortcuts import render, redirect
from .models import Reservation
from .form import RegisterForm, LoginForm
from django.contrib import messages
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
    # form = bookForm()
    # context = {}
    # context['subtitle'] = '會議室借用'
    # context['form'] = form
    return render(request, 'book.html', context)


def comfirm(request):
    return render(request, 'comfirm.html')


def forget(request):
    return render(request, 'forget.html')


def home(request):
    return render(request, 'home.html')


def participants(request):
    return render(request, 'participants.html')


def records(request):
    if request.GET.get('user-filter'):
        user_filter = request.user
        reservations = Reservation.objects.filter(reservation_=user_filter)
    else:
        messages.error(
            request, "Unsuccessful user_filter.")
        reservations = Reservation.objects.all()
    context = {}
    context['subtitle'] = '借用記錄查詢'
    context['reservations'] = reservations
    return render(request, 'records.html', context=context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auth.login(request, user)
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
    context = {}
    context['subtitle'] = '錯誤回報'
    return render(request, 'report.html', context=context)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            messages.success(request, "Login successful.")
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('/home/')
        messages.error(
            request, "Login invalid")

    form = LoginForm()
    context = {}
    context['subtitle'] = 'login'
    context['form'] = form
    return render(request, 'register.html', context)


def user_logout(request):
    auth.logout(request)
    return redirect('/home/')
