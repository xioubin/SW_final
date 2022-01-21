from django.db.models import Q
from django.contrib import auth
from django.shortcuts import render, redirect
from .models import Reservation, User_Info, ErrorReport
from .form import ModifyForm, RegisterForm, LoginForm, bookForm, forgetForm, IndexDateForm
from django.contrib import messages
import datetime

from django.core.mail import send_mail
from django.conf import settings
import random
import string
# Create your views here.

# time_choices = ['8:00-9:00', '9:00-10:00', '10:00-11:00',
#                 '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00', ]
# room_choices = [1, 2, 3, 4, 5]


def index(request):
    if request.method == "POST":
        date = request.POST['date']
        print(date)
    else:
        date = datetime.datetime.now().date()
    context = {}
    context['subtitle'] = '借用情形查詢'
    context['time_choices'] = Reservation.TIME_CHOICES
    context['room_choices'] = Reservation.ROOM_CHOICES
    context['date'] = date
    reservations = Reservation.objects.filter(date=date)
    context['reservations'] = reservations

    htmls = ""

    invalid = False

    for i, time_choice in context['time_choices']:
        htmls += f"<tr><td class='centerText'>{time_choice}</td>"
        for j, room_choice in context['room_choices']:

            htmls += f"<td timeid = {time_choice} roomid = {room_choice}>"

            invalid = False
            for reservation in reservations:
                # print(reservation.time, i)
                if(reservation.time == i and reservation.room == j):
                    invalid = True

            if(invalid):
                htmls += "<a class='centerText'>Invalid</a>"
            else:
                # htmls += "<a class='centerText'>Valid</a>"

                htmls += f"<a class='centerText' href='/home/book/?date={str(date)}&time={i}&room={j}'>Book</a>"
            htmls += "</td>"
        htmls += "</td></tr>"

    context['htmls'] = htmls
    return render(request, 'index.html', context=context)


def book(request):

    if request.method == "POST":
        form = bookForm(request.POST, user=request.user)
        if form.is_valid():
            text = 'You successfully reservated a meeting room. Please remember your meeting time.\nYour have reservated: ' + \
                request.POST.get(
                    'date') + ' at ' + Reservation.TIME_CHOICES[int(request.POST.get('time'))][1] + '\n'
            mail = request.user
            send_mail('借用成功通知', text, None, [mail])
            print(form.cleaned_data)
            send_mail('會議邀請通知', '你他媽的給我來參加會議喔', None,
                      form.cleaned_data.get('invitees'))
            form.save()
            return redirect('/home/')
    date = request.GET.get('date')
    time = request.GET.get('time')
    room = request.GET.get('room')
    form = bookForm(user=request.user, time=time, room=room, date=date)
    context = {}
    context['subtitle'] = '借用'
    context['form'] = form
    return render(request, 'book.html', context)


def modify(request):
    auto_increment_id = request.GET.get('auto_increment_id')

    reservation = Reservation.objects.get(auto_increment_id=auto_increment_id)

    if request.method == "POST":
        form = ModifyForm(request.POST, instance=reservation)
        if form.is_valid():
            print(form.cleaned_data)
            send_mail('更改會議成功', 'Your reservation has been changed. Please check on your calander.',
                      None, form.cleaned_data.get('invitees'))
            form.save()
            return redirect('/home/records/')
    print(auto_increment_id)
    print(reservation, reservation.date)
    form = ModifyForm(instance=reservation, date=reservation.date)

    context = {}
    context['subtitle'] = '借用'
    context['form'] = form
    return render(request, 'modify.html', context)


def delete(request):
    auto_increment_id = request.GET.get('auto_increment_id')
    Reservation.objects.filter(auto_increment_id=auto_increment_id).delete()
    send_mail('會議取消通知', 'Your meeting has been cancelled. Please check on your calander. ', None, [
              request.user])
    return redirect('/home/records/')


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
                print(random_password)
                user = User_Info.objects.get(email=email)
                user.set_password(random_password)
                user.save()

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
    context = {}

    if request.user.is_authenticated:
        host_reservations = Reservation.objects.filter(organizer=request.user)
        invited_reservations = Reservation.objects.filter(
            invitees=request.user)

    else:
        host_reservations = None
        invited_reservations = None

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

            user = auth.authenticate(email=email, password=password)
            messages.success(request, "Login successful.")
            if user is not None and user.is_active:
                print('login2')

                auth.login(request, user)
                next = request.GET.get('next')
                if next is None:
                    next = '/home/'
                return redirect(next)
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
