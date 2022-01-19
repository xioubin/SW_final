from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.book, name='book'),
    path('comfirm/', views.comfirm, name='comfirm'),
    path('forget/', views.forget, name='forget'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('participants/', views.participants, name='participants'),
    path('records/', views.records, name='records'),
    path('register/', views.register, name='register'),
    path('report/', views.report, name='report'),
    # path('accounts/login/', views.user_login),
]
