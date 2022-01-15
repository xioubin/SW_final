
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def get_calendar():
    time_choices = [8, 9, 10, 11, 12]
    room_choices = [1, 2, 3, 4, 5]
    return {'time_choices': time_choices, 'room_choices': room_choices}


def index(request):
    context = get_calendar()
    context['subtitle'] = '借用情形查詢'
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


def home(request):
    context = get_calendar()
    context['subtitle'] = '借用情形查詢'
    return render(request, 'home.html', context=context)


def participants(request):
    return render(request, 'participants.html')


def records(request):
    return render(request, 'records.html')


def register(request):
    return render(request, 'register.html')


def report(request):
    return render(request, 'report.html')


def search(request):
    return render(request, 'search.html')


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
