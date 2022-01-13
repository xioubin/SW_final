from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('book/', views.book),
    path('comfirm/', views.comfirm),
    path('forgrt/', views.forgrt),
    path('home/', views.home),
    path('login/', views.login),
    path('participants/', views.participants),
    path('records/', views.records),
    path('register/', views.register),
    path('report/', views.report),
    path('search/', views.search),
    path('accounts/login/', views.user_login),
]
