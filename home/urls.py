from django.urls import path
from django .contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', login_required(views.book), name='book'),
    path('book/$', login_required(views.book), name='book'),
    path('modify/$', login_required(views.modify), name='modify'),
    path('delete/$', login_required(views.delete), name='delete'),
    path('records/', login_required(views.records), name='records'),


    # path('comfirm/', views.comfirm, name='comfirm'),
    path('forget/', views.forget, name='forget'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # path('participants/', views.participants, name='participants'),
    path('register/', views.register, name='register'),
    path('report/', views.report, name='report'),

]
